class Nameable(object):
	"""Interface for an object that can be uniquely referred to by name
	"""
	def __init__(self, name):
		self._name = name
		
	def get_name(self):
		return self._name