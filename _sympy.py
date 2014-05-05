from sympy import Symbol
from sympy import abc
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
