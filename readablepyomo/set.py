from .derived import Derived
from .nameable import Nameable

class Set(Derived, Nameable):
	def __init__(self, name = ""):
		self.super_init(Nameable, name)