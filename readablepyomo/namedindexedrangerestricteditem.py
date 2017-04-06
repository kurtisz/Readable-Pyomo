from .derived import Derived
from .nameable import Nameable
from .indexable import Indexable
from .rangerestrictable import RangeRestrictable
from .util import concatenate

class NamedIndexedRangeRestrictedItem(Derived, Nameable, Indexable, RangeRestrictable):
	def __init__(self, name = ""):
		self.super_init(Nameable, name)
		self.super_init(Indexable)
		self.super_init(RangeRestrictable)
		
	def create_code(self, model_variable_name = "model", index_map = dict()):
		return model_variable_name				+	\
				"."								+	\
				self.get_name()					+	\
				self.get_index_code(index_map)