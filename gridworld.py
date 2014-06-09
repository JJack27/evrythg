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
GOAL  =  4.
WALL  =  1.

# action space $\mathcal{A}$
A_ = dict()
A_['UP']     = array([[-1], [ 0]])
A_['DOWN']   = array([[ 1], [ 0]])
A_['LEFT']   = array([[ 0], [-1]])
A_['RIGHT']  = array([[ 0], [ 1]])
A = [A_[k] for k in A_.keys()]

# utility functions
idx = lambda i: (i[0, :], i[1, :])

# initialize a small gridworld
W = FREE * ones((6, 6)) 
W[1, 1] = GOAL
W[4, 4] = GOAL

def set_border(W, w = WALL):
    for i in [0, -1]:
        W[:, i] = w
        W[i, :] = w
    return W
W = set_border(W)

def states(M = W):
    """
    Set up state space $\mathcal{S}$ consisting of all reachable non terminal states
    M: maze
    """
    return [array([[m], [n]]) for m in range(M.shape[0]) for n in range (M.shape[1]) if M[idx(array([[m], [n]]))] == FREE]

S = states()

def P(s, a, S, M = W):
    """
    State transition probability 
    s: state
    a: action
    S: successor state
    M: maze
    """
    return (M[idx(S)] != WALL) * 1.

def R(s, a, S, M = W):
    """
    Reward for transition
    s: state
    a: action
    S: successor state
    """
    if M[idx(S)] == GOAL: return  0
    if M[idx(S)] == WALL: return -2
    if M[idx(S)] == FREE: return -1

def s_0(M = W):
    """
    Random start postion
    M: maze
    """
    while True:
        s_0 = randint(0, M.shape[0], size=(2,1))
        if (M[idx(s_0)] != WALL) & (M[idx(s_0)] != GOAL):
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
    if P(s, A_['RIGHT'], s + A_['RIGHT']) > 0: return A_['RIGHT']
    else: return(random_action(s))

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

