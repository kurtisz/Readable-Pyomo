from .util import *
from .set import Set
from .sets import *
from .parameter import Parameter
from .variable import Variable
from .model import Model
from .expressions import *

def _create_model(sets = [], parameters = [], variables = []):
	model = Model()
	model.add_sets(sets)
	model.add_parameters(parameters)
	model.add_variables(variables)
	return model

def given(sets = [], parameters = [], variables = []):
	return _create_model(sets, parameters, variables)
	
def sets(*sets):
	return sets
	
def parameters(*parameters):
	return parameters
	
def variables(*variables):
	return variables