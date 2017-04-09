from pyomo.environ import AbstractModel
from .pyomosetcreator import PyomoSetCreator
from .pyomoparametercreator import PyomoParameterCreator
from .pyomovariablecreator import PyomoVariableCreator
from .pyomoobjectivecreator import PyomoObjectiveCreator
from .pyomoconstraintcreator import PyomoConstraintCreator

class PyomoModelCreator:
	@staticmethod
	def create_pyomo_abstract_model(model):
		abstract_model = AbstractModel()
		set_map = PyomoSetCreator.create_pyomo_sets(abstract_model, model.sets)
		parameter_map = PyomoParameterCreator.create_pyomo_parameters(abstract_model, set_map, model.parameters)
		variable_map = PyomoVariableCreator.create_pyomo_variables(abstract_model, set_map, model.variables)
		PyomoObjectiveCreator.create_pyomo_objective(abstract_model, set_map, parameter_map, variable_map, model.objective)
		PyomoConstraintCreator._create_pyomo_constraints(abstract_model, set_map, parameter_map, variable_map, model.constraint_comparisons)
		return abstract_model
	
	@staticmethod
	def create_pyomo_model(model, data_file):
		return PyomoModelCreator.create_pyomo_abstract_model(model).create_instance(data_file)