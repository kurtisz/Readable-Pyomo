from .pyomoitemcreator import PyomoItemCreator
from pyomo.environ import Constraint

_ABSTRACT_MODEL_VARIABLE_NAME = "model"

class PyomoConstraintCreator(object):
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
		lambda_signature = "lambda " + _ABSTRACT_MODEL_VARIABLE_NAME
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
		index_map = PyomoConstraintCreator._create_constraint_index_map(unbound_sets)
		constraint_code = constraint_comparison.create_code(_ABSTRACT_MODEL_VARIABLE_NAME, index_map)
		constraint_rule_code = PyomoConstraintCreator._create_constraint_lambda_signature_code(constraint_comparison, index_map) + " : eval(constraint_code, locals())"
		constraint_sets_code = PyomoConstraintCreator._create_constraint_sets_tuple_code(unbound_sets, "abstract_model")
		constraint_sets_tuple = eval(constraint_sets_code, locals())
		if len(constraint_sets_tuple) > 1:
			constraint = Constraint(*constraint_sets_tuple, rule = eval(constraint_rule_code, locals()))
		else:
			constraint = Constraint(constraint_sets_tuple, rule = eval(constraint_rule_code, locals()))
		abstract_model.__setattr__(constraint_name, constraint)
		
	@staticmethod
	def _create_pyomo_constraints(abstract_model, set_map, parameter_map, variable_map, constraint_comparisons):
		constraint_index = 0
		for constraint_comparison in constraint_comparisons:
			PyomoConstraintCreator._create_pyomo_constraint(abstract_model, set_map, parameter_map, variable_map, constraint_comparison, "constraint" + str(constraint_index))
			constraint_index += 1