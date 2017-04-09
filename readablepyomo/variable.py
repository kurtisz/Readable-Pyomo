from .derived import Derived
from .nameable import Nameable
from .indexable import Indexable
from .rangerestrictable import RangeRestrictable
from .evaluatable import Evaluatable

class Variable(Derived, Nameable, Indexable, RangeRestrictable, Evaluatable):
	''' A variable within the model with a name and associated set or default '''
	def __init__(self, name = ""):
		self.super_init(Nameable, name)
		self.super_init(Indexable)
		self.super_init(RangeRestrictable)
		
	def create_code(self, model_variable_name, index_map):
		return model_variable_name				+	\
				"."								+	\
				self.get_name()					+	\
				self.get_index_code(index_map)