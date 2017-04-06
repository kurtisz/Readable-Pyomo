class RangeRestrictable(object):
	def __init__(self):
		self._range = None
		
	def within(self, range):
		self._range = range
		return self
		
	def get_range(self):
		return self._range