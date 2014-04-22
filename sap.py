# sampling approach
from numpy import array
from numpy import cos
from numpy import dot
from numpy import ones
from numpy import pi
from numpy import sin
from numpy import sqrt
from numpy import sum
from numpy import vstack
from numpy import hstack
from numpy.linalg import norm
from numpy.linalg import det
from numpy.random import rand
from matplotlib.pyplot import figure
# wrpr.py
from wrpr import _scatter

def sd(P, L):
	"""
	'Signed distance:'
	'Point: '; P
	'Line:  '; L
	'Vector normal to L': N
	'Line: '; L = array([[1, 3], [4, 9]])
	'Point: '; P = array([[3, 3]])
	sd(P, L)
	_scatter(L)
	_scatter(P)
	"""
	N = array([[L[0, 1] - L[1,1]], [L[1,0] - L[0, 0]]]).squeeze()
	return dot(N / norm(N), P.squeeze() - L[0, :] ) 

def A_T(T):
	"""	
	'(Signed) Area" '
	'Triangle: T'
	from numpy import array
	T = array([[4, 0], [3, 4], [0, 1]])
	A_T(T)
	"""
	return 0.5 * det(hstack((T, ones((3, 1)))))


def R_2D(phi, p):
	"""
	'Rotation in the 2D plane'
	'Angle to rotate about: phi'
	'Points to rotate'
	R_2D(pi/2, array([[1, 0], [0, 1]]))
	"""
	return array([dot(array([[cos(phi), -sin(phi)],
	[sin(phi),  cos(phi)]]), p_) for p_ in p])

def pit(P, T):
	"""
	'Point inside triangle?'
	'Point: '; P
	'Triangle: '; T
	'Due too >= vertices are considered inside'
	'Point: '; P = array([[3, 3]])
	'Triangle: '; T = array([[4, 0], [3, 4], [0, 1]])
	pit(P, T)
	pit(T[1,:], T)
	_scatter(T)
	_scatter(P)
	"""
	return (sd(P, T[:2]) >= 0) & (sd(P, T[1:]) >= 0) & (sd(P, T[[2,0]]) >= 0)

def bcc(P, T):
	"""
	'Barycentric coordinates: '
	'Point: '; P
	'Triangle: '; T
	T = array([[4, 0], [3, 4], [0, 1]])
	P = array([[3, 3]])
	bcc(P, T)
	bcc(sum(T)/3, T)
	bcc(T[1,:], T)
	"""
	return array([sd(P, T[1:])    / sd(T[0], T[1:]),
	sd(P, T[[2,0]]) / sd(T[1], T[[2,0]]),
	sd(P, T[:2])    / sd(T[2], T[:2])])

def ss_2(T):
    """
    'Sampling scheme #2'
    'Triangle: ' T
    """
    r, s = rand(2)
    return sum(array([[1.0 - sqrt(s)],
	[(1.0 - r) * sqrt(s)],
	[r * sqrt(s)]]) * T, axis=0)

def uspit(N, T):
    """
    	'Uniformly sample points in triangle'
	'Triangle: '; T
	'Number of samples: ';  N
	N = 1000
	T = R_2D(pi/5, array([[-1, -1], [1, -1], [0, 1]]))
	_line(T)
	p_i = uspit(N, T)
    	A_T(S)
    """
    return array([ss_2(T) for n in range(N)])

def dw(p_i, v_i):
	"""
	'Displaced water particles: coordinates and volumes'
        'Coordinates of particles: '; Symbol('p_i')
	"""
        if any(p_i[:, -1]<= 0):
            w_i = p_i[p_i[:, -1] <= 0, :] # coordinates
            v_w = v_i[p_i[:, -1] <= 0, :] # volumes
	    return w_i, v_w  
        return zeros((1, 3)), 0

