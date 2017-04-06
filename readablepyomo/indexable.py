from .util import concatenate

class Indexable(object):
	def __init__(self):
		self._sets = []
		
	def over(self, *sets):
		self._sets = list(sets)
		return self
	
	def get_sets(self):
		return self._sets
		
	def get_unbound_sets(self):
		return self.get_sets()
		
	def get_index_code(self, index_map = dict()):
		if len(self.get_sets()) == 0:
			return ""
		return "["																			+	\
				concatenate(*[index_map[set] for set in self.get_sets()], separator = ",")	+	\
				"]"