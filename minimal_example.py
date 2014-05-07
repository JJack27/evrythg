from _sympy import _latex
_l = _latex()
_p = _l.out
_d = _l.symbol_names
from sympy import MatrixSymbol
from sympy import Symbol
from sympy import Matrix
X = MatrixSymbol('X', 3, 3)
_d[X]=r'\Phi_W'
