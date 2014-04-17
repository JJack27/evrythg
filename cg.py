from numpy import hstack
from numpy import ones
from numpy.linalg import det
from sympy.geometry import Line
from sympy.geometry import Point
from sympy.geometry import Triangle
from sympy.geometry import intersection
from sympy.geometry import Polygon

def A_T(T):
	"""	
	'(Signed) Area" '
	'Triangle: T'
	from numpy import array
	T = array([[4, 0], [3, 4], [0, 1]])
	A_T(T)
	from wrpr import _line
	_line(T)
	"""
	return det(hstack((T, ones((3, 1)))))

def sd(P, L):
	"""
	'Signed distance:'
	'Point: '; abc.P
	'Line:  '; abc.L
	'Vector normal to L': abc.N
	'Line: '; L = array([[1, 3], [4, 9]])
	'Point: '; P = array([[3, 3]])
	sd(P, L)
	_scatter(L)
	_scatter(P)
	"""
	N = array([[L[0, 1] - L[1,1]], [L[1,0] - L[0, 0]]]).squeeze()
	return dot(N / norm(N), P.squeeze() - L[0, :] ) 
' 5 Point/Triangle Inclusion '
def pit(P, T):
	"""
	'Point inside triangle?'
	'Point: '; abc.P
	'Triangle: '; abc.T
	'Due too >= vertices are considered inside'
	'Point: '; P = array([[3, 3]])
	'Triangle: '; T = array([[4, 0], [3, 4], [0, 1]])
	pit(P, T)
	pit(T[1,:], T)
	_scatter(T)
	_scatter(P)
	"""
	return (sd(P, T[:2]) >= 0) & (sd(P, T[1:]) >= 0) & (sd(P, T[[2,0]]) >= 0)
' 7 Barycentric coordinates '
' Barycentric coordinate system '
def bcc(P, T):
	"""
	'Barycentric coordinates: '
	'Point: '; abc.P
	'Triangle: '; abc.T
	T = array([[4, 0], [3, 4], [0, 1]])
	P = array([[3, 3]])
	bcc(P, T)
	bcc(sum(T)/3, T)
	bcc(T[1,:], T)
	"""
	return array([sd(P, T[1:])    / sd(T[0], T[1:]),
	sd(P, T[[2,0]]) / sd(T[1], T[[2,0]]),
	sd(P, T[:2])    / sd(T[2], T[:2])])

' For a triangle [...] the centroid is the average of the vertices '

' 03 Monte Carlo on Triangles '
' 6 Triangle sampling with scheme #2 '
def ss_2(T):
    """
    'Sampling scheme #2'
    'Triangle: ' abc.T
    """
    r, s = rand(2)
    return sum(array([[1.0 - sqrt(s)],
	[(1.0 - r) * sqrt(s)],
	[r * sqrt(s)]]) * T, axis=0)


def R_y(phi):
	"""
	'Rotation around Cartesian y-Axis'
	'Angle to rotate about: '; abc.phi * rad
	dot(R_y(30./180 * pi), array([0, 0, 1]))
	"""
	return array([[cos(phi), 0, sin(phi)],
	[0, 1, 0],
	[-sin(phi), 0, cos(phi)]])


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
	"""
	v = vuw(T)
	if len(v) > 0:
		return Polygon(*(v + intersection(T, Line(Point(-10, 0), Point(10, 0)))))
	return None 



"""
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
