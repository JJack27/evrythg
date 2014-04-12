# symbolic
from sympy import MatrixSymbol
from sympy import Eq
from sympy import eye
from sympy.abc import *
Phi = MatrixSymbol(r'\Phi', 5, 2)
Y = MatrixSymbol(r'Y', 5, 1)
tH = MatrixSymbol(r'\hat{\theta}(t)', 2, 1)
P = MatrixSymbol('P(t)', 2, 2)
Eq(P, (Phi * Phi.T).I)
Eq(tH, (Phi.T * Phi).I * Phi.T * Y)
# recursive estimation
I = eye(1)
K = MatrixSymbol('K(t)', 2, 1)
P_ = MatrixSymbol('P(t-1)', 2, 2)
tH_ = MatrixSymbol(r'\hat{\theta}(t-1)', 2, 1)
phi = MatrixSymbol(r'\phi(t)', 2, 1)
y = MatrixSymbol(r'y(t)', 1, 1)
Eq(tH, tH_ + K * (y - phi.T * tH_))
Eq(K, P_ * phi * (I + phi.T * P_ * phi).I)


# numeric
from numpy import array
from numpy import dot
from numpy import ones
from numpy import arange
from numpy.linalg import inv
Phi = array([ones(5), arange(5) + 1]).T
Y = array([1, 3, 3, 6, 7]).T
P_ = inv(dot(Phi.T, Phi))
tH_ = dot(dot(P_, Phi.T), Y)
phi = array([6])
y = array([7])
K = P_ * phi * inv(1 + phi.T * P_ * phi)
tH = tH_ + dot(K, y - phi.T * tH_)
