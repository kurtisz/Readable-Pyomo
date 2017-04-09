from .util import call_class_function

def _create_code(item, model_variable_name, index_map):
	''' Create Pyomo code for the given item '''
	return call_class_function(item, "create_code", str(item), *(model_variable_name, index_map))
		
def _get_unbound_sets(item):
	''' Get the unbound sets for the item '''
	return call_class_function(item, "get_unbound_sets", [])