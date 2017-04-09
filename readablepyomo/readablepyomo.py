from .util import to_list
from .sets import *
from .parameter import Parameter
from .variable import Variable
from .model import Model
from .expressions import *

def given(sets = [], parameters = [], variables = []):
	''' Create a model from its sets, parameters, and variables '''
	return Model.create(sets, parameters, variables)
	
# Helper functions, strictly for readability
sets = parameters = variables = to_list