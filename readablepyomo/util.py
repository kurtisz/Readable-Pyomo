def concatenate(*strings, separator = " "):
	''' Joins each string in a list or tuple with a defined separator '''
	if len(strings) == 0:
		return ""
	concatenated_string = strings[0]
	for i in range(1, len(strings)):
		concatenated_string += separator + strings[i]
	return concatenated_string
	
def subtract_set(minuend_set, subtrahend_set):
	''' Returns minuend_set - subtrahend_set '''
	return [item for item in minuend_set if not item in subtrahend_set]

def to_list(*items):
	''' Returns a variable number of arguments as a list '''
	return list(items)
	
def call_class_function(item, function_name, default, *args):
	'''
		Returns the result of calling the given function on the item,
		or the default if the given item does not have that function defined
	'''
	try:
		function = getattr(item, function_name)
		return function(*args)
	except AttributeError:
		return default