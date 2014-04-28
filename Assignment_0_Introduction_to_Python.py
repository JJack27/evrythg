from random import sample
from numpy import arange

def list_of_sets(min_val, max_val, k, l):
	"""
	l: number of lists
	k: number of elements in one list
	min_val=1;
	max_val=6;
	k=3;
	l=3;
	list_of_sets(min_val, max_val, k, l)
	min_val=1;
	max_val=3;
	k=4;
	list_of_sets(min_val, max_val, k, l)
	"""
	if k > max_val - min_val + 1: raise IndexError('Can\'t return %s unique integers \\in [%s, %s]' %(k, min_val, max_val))
	v = arange(min_val, max_val+1)
	return [set(sample(v, k)) for _ in range(l)]

from sympy import gamma
from sympy import pi
def sphere_surface_area(n_dimensions):
	"""
	n_dimensions = 3
	r = 1
	sphere_surface_area(n_dimensions)(r)
	n_dimensions = 17
	r = 1.338
	sphere_surface_area(n_dimensions)(r)
	"""
	return lambda r : float(2 * (pi ** (n_dimensions / 2.)) / gamma(n_dimensions / 2.)) * (r ** (n_dimensions - 1))
