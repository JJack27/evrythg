# coding: utf-8

from numpy import array
from matplotlib.pyplot import figure
from matplotlib.pyplot import title
from matplotlib.pyplot import imshow
from numpy.random import rand
from numpy import ndenumerate

execfile('gridworld.py')
execfile('dynamic_programming.py')

close('all')


M = array([
[1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 1, 0, 1, 0, 0, 1], 
[1, 0, 1, 0, 1, 1, 0, 1], 
[1, 0, 1, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 1, 0, 0, 1], 
[1, 0, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 1], 
[1, 1, 1, 1, 1, 1, 1, 1] 
])
EPSILON = 0.1
ALPHA = 0.9
GAMMA = 1
M[idx(array([[4],[6]]))] = GOAL

def step(s, a, M):
    """
    s: current state
    a: action
    """
    S = S_(s, a, M)
    return S, R(s, a, S, M)

def eps_greedy(s, Q):
    """
    $\epsilon$ greedy strategy
    s: state
    """
    if rand() < EPSILON:
        return randint(0, len(A))
    else:
        return argmax([Q[(a, s[0], s[1])] for a in range(len(A))])

def sarsa(W=W):
    """
    cf. 140602214446
    """
    Q = ones((len(A), W.shape[0], W.shape[1]))
    for (m, n), value in ndenumerate(M): 
        if M[(m, n)] == GOAL:
            Q[(tuple(range(len(A))), m, n)] = 0 
    for i in range(1000):
        s = s_0(W)
        a = eps_greedy(s, Q)
        while W[idx(s)] != GOAL:
            s_, r = step(s, A[a], W)
            a_ = eps_greedy(s_, Q)
            Q[(a, s[0], s[1])] = Q[(a, s[0], s[1])] + ALPHA * (r + GAMMA * Q[(a_, s_[0], s_[1])] - Q[(a, s[0], s[1])])
            s = s_
            a = a_
    return Q

def visualize():
    i = argmax(Q, axis=0)
    for (m ,n), value in ndenumerate(i): # iterate arran obtaining 2D indices
        if M[(m, n)] == WALL: i[(m, n)] = -1 # blank out walls
        if M[(m, n)] == GOAL: i[(m, n)] = GOAL  # mark goal
        imshow(i, interpolation='nearest')
    return i

Q = sarsa(M)
figure()
title('The maze')
imshow(M, interpolation='nearest')
figure()
title('$Q$ function')
I = visualize()

