class RangeRestrictable(object):
	''' Object which can be restricted to a particular range (e.g. x.within(NonNegativeReals)) '''
	def __init__(self):
		self._range = None
		
	def within(self, range):
		self._range = range
		return self
		
	def get_range(self):
		return self._range