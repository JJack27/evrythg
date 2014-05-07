from sympy import Symbol
from sympy import abc
from sympy.printing import latex
# tex_magic.py
from tex_magic import TeX1 
def _s(expr):
	"""
	Show Latex in QT Console
	Expression: expr
	"""
	expr = str(expr)
    	if not expr.startswith('$'): expr = '$%s$' %(expr)
	expr = expr.replace(r'\limits', '')
	expr = expr.replace('==', '=')
	expr = expr.replace('**', '^')
	expr = expr.replace('*', '')
	return TeX1(str(expr), color='red')

def _idx(expr, i='i'):
	"""
	Add an index to expression
	Expression: expr
	Index: i
	_idx(r)
	"""	
	return Symbol(str(expr) + '_{%s}' %(i))
def _d(v):
	"""
	Differential
	Variable: v
	"""	
	return Symbol(r'\operatorname{d} %s' %(v))

class _latex:
    """
    Print a latex representation with special symbols replaced
    symbol_names: the dictionary containing replacements
    """
    def __init__(self):
        self.symbol_names = dict() 
    def out(self, expr):
        """
        expr: A sympy expression
        _l = _latex()
        _p = _l.out
        _d = _l.symbol_names
        from sympy import MatrixSymbol
        from sympy import Symbol
        from sympy import Matrix
        X = MatrixSymbol('X', 3, 3)
        _d[X]=r'\Phi_W'
        _p(Matrix([[X], [X]]))
        k = Symbol('k')
        _d[k]=r'\k_W'
        _p(Sum(X * k, (k, 1, 10)))
        """
	l = latex(expr, symbol_names=self.symbol_names)
        print(l)
	return l

