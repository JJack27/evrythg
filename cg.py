from numpy import hstack
from numpy import ones
from numpy.linalg import det
from sympy.geometry import Line
from sympy.geometry import Point
from sympy.geometry import Triangle
from sympy.geometry import intersection
from sympy.geometry import Polygon



def vuw(T):
	"""
	Vertices under water
	Triangle: T
	"""
	return [v for v in T.vertices if v.y <= 0]

def auw(T):
	""" 
	Area under water
	Triangle: T
	Waterlevel assumed to be at 0
	o = Point(-1, -1)
	p = Point(1, -1)
	q = Point(0, 1)
	T = Triangle(o, p, q)
	vuw(T)
	r = Point(-1, 1)
	s = Point(1, 1)
	t = Point(0, 2)
	V = Triangle(r, s, t)
	vuw(V)
	auw(V)
	from wpr import _pp
	figure()
	_pp(T)
	_pp(auw(T), color='g')
	"""
	v = vuw(T)
	if len(v) > 0:
		return Polygon(*(v + intersection(T, Line(Point(-10, 0), Point(10, 0)))))
	return None 



