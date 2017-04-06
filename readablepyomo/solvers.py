from pyomo.environ import AbstractModel
from pyomo.environ import Set as PyomoSet
from pyomo.environ import Param
from pyomo.environ import Var
from pyomo.environ import SolverFactory
from pyomo.environ import Constraint
from pyomo.environ import minimize, maximize
from .sets import NonNegativeReals, PositiveIntegers, NonNegativeIntegers
import pyomo.environ
from .objective import Objective

class PyomoModelCreator:
	_sense_translations = { Objective.Sense.MINIMIZE: minimize, Objective.Sense.MAXIMIZE: maximize}
	
	@staticmethod
	def _create_pyomo_item(pyomo_item_creator, pyomo_item_creator_arg):
		return pyomo_item_creator(pyomo_item_creator_arg)

	@staticmethod
	def _set_abstract_model_property(abstract_model, property_name, value):
		abstract_model.__setattr__(property_name, value)
		
	@staticmethod
	def _create_and_set_abstract_model_property_item(abstract_model, property_name, pyomo_item_creator, pyomo_item_creator_arg):
		# Create the Pyomo item
		pyomo_item = PyomoModelCreator._create_pyomo_item(pyomo_item_creator, pyomo_item_creator_arg)
		# Set the property to the created item
		PyomoModelCreator._set_abstract_model_property(abstract_model, property_name, pyomo_item)
		return pyomo_item
		
	@staticmethod
	def _create_and_set_abstract_model_indexed_property_item(abstract_model, property_name_base, property_name_index, pyomo_item_creator, pyomo_item_creator_arg):
		return PyomoModelCreator._create_and_set_abstract_model_indexed_property_item(abstract_model, property_name_base + property_name_index, pyomo_item_creator, pyomo_item_creator_arg)
		
	@staticmethod
	def _create_and_set_abstract_model_indexed_property_item(abstract_model, nameable, property_name_base, property_name_index, pyomo_item_creator, pyomo_item_creator_arg):
		name = nameable.get_name()
		if len(name) > 0:
			return PyomoModelCreator._create_and_set_abstract_model_property_item(abstract_model, name, pyomo_item_creator, pyomo_item_creator_arg)
		else:
			return PyomoModelCreator._create_and_set_abstract_model_indexed_property_item(abstract_model, property_name_base, property_name_index, pyomo_item_creator, pyomo_item_creator_arg)
	
	@staticmethod
	def _create_pyomo_sets(abstract_model, sets):
		set_map = {NonNegativeReals: pyomo.environ.NonNegativeReals, PositiveIntegers: pyomo.environ.PositiveIntegers, NonNegativeIntegers: pyomo.environ.NonNegativeIntegers}
		i = 0
		for set in sets:
			pyomo_set_creator = lambda set : PyomoSet()
			set_map[set] = PyomoModelCreator._create_and_set_abstract_model_indexed_property_item(abstract_model, set, "set", i, pyomo_set_creator, None)
			i = i + 1
		return set_map
	
	@staticmethod
	def _create_pyomo_indexable_item_creator(indexable_type):
		def _create_pyomo_indexable_type_item(indexable_item_dict):
			if len(indexable_item_dict["sets"]) > 0:
				if indexable_item_dict["default"] is None:
					return indexable_type(*indexable_item_dict["sets"], within=indexable_item_dict["range"])
				else:
					return indexable_type(*indexable_item_dict["sets"], within=indexable_item_dict["range"], default=indexable_item_dict["default"])
			else:
				if indexable_item_dict["default"] is None:
					return indexable_type(within=indexable_item_dict["range"])
				else:
					return indexable_type(within=indexable_item_dict["range"], default=indexable_item_dict["default"])
		return _create_pyomo_indexable_type_item
		
	@staticmethod
	def _create_pyomo_indexable_item(abstract_model, set_map, indexable_items, property_base_name, indexable_item_type):			
		map = dict()
		i = 0
		for indexable_item in indexable_items:
			default = None
			if "get_default" in dir(indexable_item):
				default = indexable_item.get_default()
			indexable_item_arguments = {"sets": [set_map[set] for set in indexable_item.get_sets()], "range": set_map[indexable_item.get_range()], "default": default}
			map[indexable_item] = PyomoModelCreator._create_and_set_abstract_model_indexed_property_item(abstract_model, indexable_item, property_base_name, i, PyomoModelCreator._create_pyomo_indexable_item_creator(indexable_item_type), indexable_item_arguments)
			i = i + 1
		return map
		
	@staticmethod
	def _create_pyomo_objective(abstract_model, set_map, parameter_map, variable_map, objective):
		objective_sense = PyomoModelCreator._sense_translations[objective.get_sense()]
		abstract_model.cost = pyomo.environ.Objective(rule = objective.create_func(), sense = objective_sense)
	
	@staticmethod
	def _create_constraint_index_map(unbound_sets):
		index_map = dict()
		unbound_set_index_num = 0
		for unbound_set in unbound_sets:
			index_map[unbound_set] = "cindex" + str(unbound_set_index_num)
			unbound_set_index_num += 1
		return index_map
		
	@staticmethod
	def _create_constraint_lambda_signature_code(constraint_comparison, index_map):
		lambda_signature = "lambda model"
		for unbound_set in set(constraint_comparison.get_unbound_sets()):
			lambda_signature += ", " + index_map[unbound_set]
		return lambda_signature
		
	@staticmethod
	def _create_constraint_sets_tuple_code(unbound_sets, model_variable_name):
		code = "("
		i = 0
		while i < len(unbound_sets):
			if i > 0:
				code += ","
			code += model_variable_name + "." + unbound_sets[i].get_name()
			i += 1
		code += ")"
		return code
		
	@staticmethod
	def _create_pyomo_constraint(abstract_model, set_map, parameter_map, variable_map, constraint_comparison, constraint_name):
		unbound_sets = list(set(constraint_comparison.get_unbound_sets()))
		index_map = PyomoModelCreator._create_constraint_index_map(unbound_sets)
		constraint_code = constraint_comparison.create_code("model", index_map)
		constraint = None
		constraint_rule_code = PyomoModelCreator._create_constraint_lambda_signature_code(constraint_comparison, index_map) + " : eval(constraint_code, locals())"
		constraint_sets_code = PyomoModelCreator._create_constraint_sets_tuple_code(unbound_sets, "abstract_model")
		constraint = Constraint(eval(constraint_sets_code, locals()), rule = eval(constraint_rule_code, locals()))
		abstract_model.__setattr__(constraint_name, constraint)
		
	@staticmethod
	def _create_pyomo_constraints(abstract_model, set_map, parameter_map, variable_map, constraint_comparisons):
		constraint_index = 0
		for constraint_comparison in constraint_comparisons:
			PyomoModelCreator._create_pyomo_constraint(abstract_model, set_map, parameter_map, variable_map, constraint_comparison, "constraint" + str(constraint_index))
			constraint_index += 1

	@staticmethod
	def create_pyomo_model(model):
		abstract_model = AbstractModel()
		set_map = PyomoModelCreator._create_pyomo_sets(abstract_model, model.sets)
		parameter_map = PyomoModelCreator._create_pyomo_indexable_item(abstract_model, set_map, model.parameters, "parameter", Param)
		variable_map = PyomoModelCreator._create_pyomo_indexable_item(abstract_model, set_map, model.variables, "variable", Var)
		PyomoModelCreator._create_pyomo_objective(abstract_model, set_map, parameter_map, variable_map, model.objective)
		PyomoModelCreator._create_pyomo_constraints(abstract_model, set_map, parameter_map, variable_map, model.constraint_comparisons)
		return abstract_model

class Solver:
	@staticmethod
	def solve(solver, model, data_file):
		abstract_model = PyomoModelCreator.create_pyomo_model(model)
		return solver.solve(abstract_model.create_instance(data_file), load_solutions=False)

class Glpk:
	@staticmethod
	def solve(model, data_file):
		return Solver.solve(SolverFactory("glpk"), model, data_file)