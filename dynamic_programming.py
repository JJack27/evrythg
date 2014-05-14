
# coding: utf-8


execfile('gridworld.py')



def wrapper(func, *args, **kwargs):
    """
    Wrap function (handling keyword arguments)
    """
    def wrapped():
        return func(*args, **kwargs)
    return wrapped



from numpy import set_printoptions
from numpy.linalg import norm
from numpy import sum
from numpy import argmax
from timeit import timeit
from matplotlib.pyplot import arrow
from numpy import float



get_ipython().magic(u'matplotlib')



# Convergence criterion
converged = lambda V, _V:  norm(V - _V) < 1e-1



# Update value function
_v = lambda s, a, S, V: P(s, a, S) * (R(s, a, S) + 1. * V[idx(S)])



def S_(s, a):
	"""
	Next state
	"""
	if P(s, a, s + a) > 0:
		return s + a
	else:
		return s



def PU(V, PI):
    """
    Policy update
    """
    PI = PI * 0
    for s_ in S:
        PI[s_[0], s_[1], argmax(array([_v(s_, a, S_(s_, a), V) for a in A]))] = 1;
    print 'Running policy update'
    return PI



def P_E(PI, V):
    """
    Synchronous policy evaluation
    """
    _V = zeros(V.shape) 
    i = 0
    while True:
            i = i + 1
            for s_ in S:
                _V[idx(s_)] = sum(PI[idx(s_)] * array([_v(s_, a, S_(s_, a), V) for a in A]).T)
            if converged(V, _V): break 
            V = _V.copy()
    print 'Policy evaluation converged after %d iterations' %i
    return _V



def SPI():
    """
    Synchronous policy iteration
    """
    PI = 1./ len(A) * ones((W.shape[0], W.shape[1], len(A)))
    V = P_E(PI, zeros(W.shape))
    while True:
        PI_ = PU(V, PI.copy())
        if converged(PI, PI_): break 
        PI = PI_.copy()
        V = P_E(PI, V)
    return V, PI



def SVI():
    """
    Synchronous value iteration
    """
    V = zeros(W.shape)
    _V = zeros(W.shape)
    i = 0
    while True:
        i = i + 1
        for s_ in S:
            v = array([_v(s_, a, S_(s_, a), V) for a in A])
            _V[idx(s_)] = v[argmax(v)]
        if converged(V, _V): break 
        V = _V.copy()
    print 'Value iteration converged after %d iterations' %i
    return V




set_printoptions(precision = 3)
print 'Policy iteration takes %s [sec]' %timeit(SPI, number=1)




set_printoptions(precision = 3)
print 'Value iteration takes %s [sec]' %timeit(SVI, number=1)



PI = SPI()[1]






def vp(PI):
    """
    Visualize policy
    """
    P = zeros(W.shape)
    for s_ in S:
        x, y = s_
        i = argmax(PI[x, y])
        P[x, y] = i+10
        #arrow(float(x), float(y), -0.9 * float(A[i][0]), -0.9 *float(A[i][1]),head_width = 0.05, head_length = 0.1, length_includes_head = True)
    imshow(P, interpolation='nearest')



vp(PI)





