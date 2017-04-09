import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from readablepyomo.readablepyomo import *
from readablepyomo.glpk import Glpk

Food = Set("F")
Nutrients = Set("N")

c = Parameter("c").over(Food).within(NonNegativeReals)
a = Parameter("a").over(Food, Nutrients).within(NonNegativeReals)
Nmin = Parameter("Nmin").over(Nutrients).within(NonNegativeReals).with_default(0.0)
Nmax = Parameter("Nmax").over(Nutrients).within(NonNegativeReals).with_default(float('inf'))
V = Parameter("V").over(Food).within(NonNegativeReals)
Vmax = Parameter("Vmax").within(NonNegativeReals)

x = Variable("x").over(Food).within(NonNegativeIntegers)

Glpk.solve(
	given(
			sets(Food, Nutrients),
			parameters(c, a, Nmin, Nmax, V, Vmax),
			variables(x)
		) 																	\
		.minimize(sum_over(Food)(c * x)) 									\
		.such_that(sum_over(Food)(a * x).is_within(Nmin, Nmax)) 			\
		.such_that(sum_over(Food)(V * x).is_less_than_or_equal_to(Vmax)),
		"diet.dat"
	).write()