from numpy import array
from sympy.geometry import Point
from sympy.geometry import Triangle
from matplotlib.pyplot import close
from matplotlib.pyplot import plot
from matplotlib.pyplot import legend
from matplotlib.pyplot import grid
from matplotlib.pyplot import savefig
from numpy import mean
from numpy import arange
# wrpr.py
from wrpr import _line
from wrpr import _scatter
from wrpr import _arrow
from wrpr import _pp
from cg import  auw
# clean_sym.py
import clean_sym as sym
# clean_numeric_values.py
import clean_numeric_values as n
# sap.py
from sap import *
o = Point(-1, -1)
p = Point(1, -1)
q = Point(0, 1)
T = Triangle(o, p, q).rotate(pi/5.)
C_W = array([T.centroid.x, T.centroid.y]).astype(float)
D = auw(T)
C_B = array([D.centroid.x, D.centroid.y]).astype(float)
g = array([0, -1])
W =  float(T.area) * n.rho 
B =  - float(D.area) * 1 
figure()
_pp(T)
_pp(D, color='g')
_arrow(C_W, g*W, label='$%s$' %sym.W)
_arrow(C_B, g*B, label='$%s$' %sym.B, color='g')
_scatter(C_W, color='b', label='$%s$' %sym.C_W)
_scatter(C_B, color='g', label='$%s$' %sym.C_B)
legend(scatterpoints=1)
grid()
savefig('triangle.pdf')
close('all')
T = R_2D(pi/5, array([[-1, -1], [1, -1], [0, 1]]))
p_i = uspit(n.N, T)
v_i =  A_T(T) / n.N * ones((p_i.shape[0], 1))
w_i, v_w = dw(p_i, v_i)  
_line(T)
C_B = mean(w_i, axis=0)
C_W = mean(p_i, axis= 0)
g = array([0, -1])
B = sum(v_w) * -1. * g
W = sum(v_i) * n.rho * g
_arrow(C_W, W, label=r'$\tilde{%s}$' %sym.W)
_arrow(C_B, B, label=r'$\tilde{%s}$' %sym.B, color='g')
_scatter(C_W, color='b', label=r'$\tilde{%s}$' %sym.C_W)
_scatter(C_B, color='g', label=r'$\tilde{%s}$' %sym.C_B)
_scatter(w_i.take(arange(0, w_i.shape[0], n.K), axis=0), color = 'g')
legend(scatterpoints=1)
grid()
savefig('triangle_tilde.pdf')
# _sympy.py
from _sympy import _latex
_l = _latex()
_p = _l.out
_d = _l.symbol_names
from sympy import MatrixSymbol
from sympy import Symbol
from sympy import Matrix
X = MatrixSymbol('X', 3, 3)
_d[X]=r'\Phi_W'
k = Symbol('k')
_d[k]=r'\Phi_k_W'
