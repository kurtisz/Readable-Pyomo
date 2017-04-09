'''
	Many classes are dependent on Evaluatable, including
	expressions. Since Evaluatable is also dependent on the
	expressions, the Evaluatable stub is defined here, and
	the rest of the class is defined in Evaluatable. This
	file should only be referenced if needed due to cyclic
	dependencies.
'''

class Evaluatable:
	''' Abstract base class for an item that can be evaluated in an expression '''
	pass