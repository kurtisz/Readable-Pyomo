class Derived(object):
	"""Simplified interface for an object that derives from another class
	"""
	def super_init(self, type, *args):
		return type.__init__(self, *args)