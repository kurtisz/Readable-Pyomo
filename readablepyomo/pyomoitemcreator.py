from .util import call_class_function

_SETS_INDEX_KEY = "sets"
_RANGE_INDEX_KEY = "range"
_DEFAULT_INDEX_KEY = "default"

class PyomoItemCreator(object):
	''' Helper class for creating various Pyomo items '''
	@staticmethod
	def _create_pyomo_item(pyomo_item_creator, pyomo_item_creator_arg):
		return pyomo_item_creator(pyomo_item_creator_arg)

	@staticmethod
	def _set_abstract_model_property(abstract_model, property_name, value):
		abstract_model.__setattr__(property_name, value)
		
	@staticmethod
	def _create_and_set_abstract_model_property_item(abstract_model, property_name, pyomo_item_creator, pyomo_item_creator_arg):
		# Create the Pyomo item
		pyomo_item = PyomoItemCreator._create_pyomo_item(pyomo_item_creator, pyomo_item_creator_arg)
		# Set the property to the created item
		PyomoItemCreator._set_abstract_model_property(abstract_model, property_name, pyomo_item)
		return pyomo_item
		
	@staticmethod
	def _create_and_set_abstract_model_indexed_property_item(abstract_model, property_name_base, property_name_index, pyomo_item_creator, pyomo_item_creator_arg):
		return PyomoItemCreator._create_and_set_abstract_model_indexed_property_item(abstract_model, property_name_base + property_name_index, pyomo_item_creator, pyomo_item_creator_arg)
		
	@staticmethod
	def create_and_set_abstract_model_indexed_property_item(abstract_model, nameable, property_name_base, property_name_index, pyomo_item_creator, pyomo_item_creator_arg):
		name = nameable.get_name()
		if len(name) > 0:
			return PyomoItemCreator._create_and_set_abstract_model_property_item(abstract_model, name, pyomo_item_creator, pyomo_item_creator_arg)
		else:
			return PyomoItemCreator._create_and_set_abstract_model_indexed_property_item(abstract_model, property_name_base, property_name_index, pyomo_item_creator, pyomo_item_creator_arg)
			
	@staticmethod
	def _create_pyomo_indexable_item_creator(indexable_type):
		def _create_pyomo_indexable_type_item(indexable_item_dict):
			if len(indexable_item_dict[_SETS_INDEX_KEY]) > 0:
				if indexable_item_dict[_DEFAULT_INDEX_KEY] is None:
					return indexable_type(*indexable_item_dict[_SETS_INDEX_KEY], within=indexable_item_dict[_RANGE_INDEX_KEY])
				else:
					return indexable_type(*indexable_item_dict[_SETS_INDEX_KEY], within=indexable_item_dict[_RANGE_INDEX_KEY], default=indexable_item_dict[_DEFAULT_INDEX_KEY])
			else:
				if indexable_item_dict[_DEFAULT_INDEX_KEY] is None:
					return indexable_type(within=indexable_item_dict[_RANGE_INDEX_KEY])
				else:
					return indexable_type(within=indexable_item_dict[_RANGE_INDEX_KEY], default=indexable_item_dict[_DEFAULT_INDEX_KEY])
		return _create_pyomo_indexable_type_item
		
	@staticmethod
	def create_pyomo_indexable_items(abstract_model, set_map, indexable_items, property_base_name, indexable_item_type):			
		map = dict()
		for i in range(len(indexable_items)):
			indexable_item = indexable_items[i]
			default = call_class_function(indexable_item, "get_default", None)
			indexable_item_arguments = {
											_SETS_INDEX_KEY: [set_map[set] for set in indexable_item.get_sets()],
											_RANGE_INDEX_KEY: set_map[indexable_item.get_range()],
											_DEFAULT_INDEX_KEY: default
										}
			map[indexable_item] = PyomoItemCreator.create_and_set_abstract_model_indexed_property_item(abstract_model,
																										indexable_item,
																										property_base_name,
																										i,
																										PyomoItemCreator._create_pyomo_indexable_item_creator(indexable_item_type),
																										indexable_item_arguments)
		return map