from .namedindexedrangerestricteditem import NamedIndexedRangeRestrictedItem
from .evaluatable import Evaluatable

class Parameter(NamedIndexedRangeRestrictedItem, Evaluatable):
	def __init__(self, name = ""):
		self.super_init(NamedIndexedRangeRestrictedItem, name)
		self.default = None
		
	def with_default(self, value):
		self.default = value
		return self
		
	def get_default(self):
		return self.default