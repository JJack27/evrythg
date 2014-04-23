from sympy import Symbol
# _sympy.py
from _sympy import _idx
k = Symbol('k') # Step index
r = Symbol('r') # reward
r_k = _idx(Symbol('r'), k) 
Q_k = _idx(Symbol('Q'), k) # Average of the first k rewards
alpha = Symbol('alpha') # step size parameter

