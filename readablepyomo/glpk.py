from .derived import Derived
from .solver import Solver

class Glpk(Derived, Solver):
	''' Convenience wrapper for the GLPK solver '''
	
	@staticmethod
	def solve(model, data_file = None):
		return Glpk().solve_instance(model, data_file)
		
	def __init__(self):
		self.super_init(Solver, "glpk")