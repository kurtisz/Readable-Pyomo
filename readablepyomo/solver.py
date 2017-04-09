from .pyomomodelcreator import PyomoModelCreator
from pyomo.environ import SolverFactory

class Solver:
	''' Solver for an RP model that passes through to a Pyomo solver '''
	
	@staticmethod
	def solve(solver, model, data_file):
		return solver.solve(PyomoModelCreator.create_pyomo_model(model, data_file), load_solutions=False)
		
	def __init__(self, name):
		self._name = name
		
	def solve_instance(self, model, data_file):
		return Solver.solve(SolverFactory(self._name), model, data_file)