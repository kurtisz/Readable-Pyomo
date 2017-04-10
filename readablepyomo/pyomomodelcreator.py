from pyomo.environ import AbstractModel, ConcreteModel
from .pyomosetcreator import PyomoSetCreator
from .pyomoparametercreator import PyomoParameterCreator
from .pyomovariablecreator import PyomoVariableCreator
from .pyomoobjectivecreator import PyomoObjectiveCreator
from .pyomoconstraintcreator import PyomoConstraintCreator

class PyomoModelCreator:
	@staticmethod
	def create_pyomo_model(model):
		if len(model.sets) > 0 or len(model.parameters) > 0:
			pyomo_model = AbstractModel()
		else:
			pyomo_model = ConcreteModel()
		set_map = PyomoSetCreator.create_pyomo_sets(pyomo_model, model.sets)
		parameter_map = PyomoParameterCreator.create_pyomo_parameters(pyomo_model, set_map, model.parameters)
		variable_map = PyomoVariableCreator.create_pyomo_variables(pyomo_model, set_map, model.variables)
		PyomoObjectiveCreator.create_pyomo_objective(pyomo_model, set_map, parameter_map, variable_map, model.objective)
		PyomoConstraintCreator.create_pyomo_constraints(pyomo_model, set_map, parameter_map, variable_map, model.constraint_comparisons)
		return pyomo_model
	
	@staticmethod
	def fill_pyomo_model(model, data_file):
		return PyomoModelCreator.create_pyomo_model(model).create_instance(data_file)