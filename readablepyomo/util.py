def _concatenate_item(item, separator = ""):
	if type(item) == type([]):
		return concatenate(*item, separator)
	return item

def concatenate(*strings, separator = ""):
	if len(strings) == 0:
		return ""
	concatenated_string = _concatenate_item(strings[0], separator)
	for i in range(1, len(strings)):
		concatenated_string += separator + _concatenate_item(strings[i], separator)
	return concatenated_string
	
def subtract_set(minuend_set, subtrahend_set):
	return [item for item in minuend_set if not item in subtrahend_set]