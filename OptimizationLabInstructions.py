from sympy import Symbol
from sympy import Function
from sympy import Eq
from _sympy import _idx

n = Symbol('n', Integer=True) # dimensions of x

h = Symbol('h') # channel coefficient
x = Symbol('x') # channel input
y = Symbol('y') # channel output
eta = Symbol(r'\eta') # channel noise
sigma = Symbol(r'\sigma') # noise variance
c = Symbol('c') # channel capacity
gamma = Symbol(r'\gamma') # channel quality
p = Symbol('p') # available power
r = Symbol('r') # channel rate
mu = Symbol(r'\mu')
e_1_1 = Eq(_idx(y), _idx(h) * _idx(x) + _idx(eta)) 
Eq(_idx(gamma), abs(_idx(h))**2 / _idx(sigma)**2)

m = Symbol('m', Integer=True) # dimensions of y
H = MatrixSymbol('H', m, n) # channel gain matrix
I = Function('I')(x, y) # mutual information
C_eta = Symbol(r'C_{\eta}') # noise covariance matrix
Q = MatrixSymbol(r'Q', n, n) # input covariance matrix
X = Symbol('X')
N = Symbol('N') # maximal sum noise power
Eq(X, H * Q * (H.T).conjugate())
R = Symbol('R') # achievable rate
psi = MatrixSymbol(r'\psi', n, 1) # eigenvalue of X
sigma = MatrixSymbol(r'\psi', m, 1) # eigenvalue of C_eta
mu = Symbol(r'\mu') # Lagrangian multiplier corresponding to the inequality constraint
