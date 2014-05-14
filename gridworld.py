from numpy import array
from numpy import ones
from numpy import zeros
from matplotlib.pyplot import imshow
from matplotlib.pyplot import figure
from matplotlib.pyplot import colorbar
from matplotlib.pyplot import close
from matplotlib.pyplot import title
from numpy.random import randint
from numpy import sum
from numpy import ravel_multi_index
from numpy import unravel_index
# constants
FREE  =  0.
GOAL  =  1.
WALL  = -1.
A_ = dict()
A_['UP']    = array([[-1], [ 0]])
A_['DOWN']  = array([[ 1], [ 0]])
A_['LEFT']  = array([[ 0], [-1]])
A_['RIGHT']  = array([[ 0], [ 1]])
A = [A_[k] for k in A_.keys()]
# utility functions
idx = lambda i: (i[0, :], i[1, :])
# setup
W = FREE * ones((6, 6)) # gridworld
W[1, 1] = GOAL
W[4, 4] = GOAL
for w in [0, -1]:
    W[:, w] = WALL
    W[w, :] = WALL

#all reachable non terminal states
S = [array([[m], [n]]) for m in range(W.shape[0]) for n in range (W.shape[1]) if W[idx(array([[m], [n]]))] == FREE]


def P(s, a, S):
    """
    Probability of state transition
    s: state
    a: action
    S: successor state
    """
    return (W[idx(S)] != WALL) * 1.

def R(s, a, S):
    """
    Reward for transition
    s: state
    a: action
    S: successor state
    """
    return -1

def s_0():
    """
    Random start postion
    """
    while True:
        s_0 = randint(0, W.shape[0], size=(2,1))
        if (W[idx(s_0)] != WALL) & (W[idx(s_0)] != GOAL):
            return s_0

def sd(pi):
    """
    Sample stationary distribution
    """
    V = zeros(W.shape)
    s = s_0()
    V[idx(s)] = V[idx(s)] + 1
    for i in range(1000):
        a = pi(s)
        p = P(s, a, s + a)
        if p > 0:
            s = s + a
            if W[idx(s)] == GOAL:
                s = s_0()
        V[idx(s)] = V[idx(s)] + 1
    return V/sum(V)

def random_action(s):
    """
    Random policy
    """
    return A[randint(0, len(A))]

def pi(s):
    """
    Move right if possible
    """
    if P(s, RIGHT, s + RIGHT) > 0: return RIGHT
    else: return(random_action(s))

if False:
	close('all')
	figure()
	title('Random policy')
	imshow(sd(random_action), interpolation='nearest')
	cb = colorbar()
	cb.set_clim(0, 0.3)
	figure()
	title('Move right if possible')
	imshow(sd(pi), interpolation='nearest')
	cb = colorbar()
	cb.set_clim(0, 0.3)

