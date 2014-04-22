# _sympy.py 
from _sympy import _idx
from _sympy import _d
from sympy import Symbol
from sympy import Derivative
from sympy import Function
from sympy import abc

# Cartesian unit vectors
i = Symbol(r'\mathbf{i}') # unit vector along x-Axis
j = Symbol(r'\mathbf{j}') # unit vector along y-Axis
k = Symbol(r'\mathbf{k}', commutative=False) # unit vector along z-Axis
G = Symbol(r'\mathcal{G}') # Geometry
V = Symbol(r'V') # Volume
Vi = _d(V) # infinitesimal volume
V_i = _idx(V) # discretization of V
D = Symbol(r'\mathcal{D}') # Geometry of displaced water
Di = _d(G) # infinitesimal volume
rho = Symbol(r'\rho') # mass density
rho_W = Symbol(r'\rho_W') # mass density of water
rhoi = Symbol(r'\operatorname{d}%s' %(rho)) # infinitesimal mass density
rho_i = _idx(rho) # discretization of rhoi
M = Symbol(r'M') # mass
Mi = Symbol(r'\operatorname{d} %s' %(M)) # infinitesimal masses
M_i = Symbol(r'\operatorname{d} %s' %(M)) # infinitesimal masses
W = Symbol(r'W') # gravity force
Wi = Symbol(r'\operatorname{d} %s' %(W)) # infinitesimal gravity forces
B = Symbol(r'B') # buoyant force
C_W = Symbol(r'C_W') # center of gravity 
C_B = Symbol(r'C_B') # center of buoyancy
X = Symbol(r'X') # unknown force
F = Symbol(r'F') # total force
g = Symbol(r'g') # earth acceleration
t = Symbol('t') # time
s = Function(r's')(t) # state vector
sdot = Derivative(s, t)
sddot = Derivative(s, Symbol('t'),2)
f = Function('\operatorname{f}')(s, sdot) # total force as a function
h = Function('\operatorname{h}')(F) # change of state 
ss = Symbol(r's^*') # state vector in equilibrium
P_xz = Symbol(r'\mathcal{P}_{x,z}') # x-z-Plane
A_xz = Symbol(r'A_{x,z}') # Area in the x-z-plane 
A_i = Symbol(r'A_{i}') # Area of a planar shape
S_i = Symbol(r'\mathcal{S}_{i}') # Planar shape 
T_i = Symbol(r'\mathcal{T}_{i}') # Planar triangle
VA = Symbol(r'A') # Vertex 
VB = Symbol(r'B') # Vertex 
VC = Symbol(r'C') # Vertex 
c = Symbol(r'\mathsf{c}', commutative=False) # some constant
r = Symbol('r') # position
ri = Symbol(r'\operatorname{d} %s' %(r)) # infinitesimal position element
x = Symbol('x') # x-coordinate
y = Symbol('y') # y-coordinate
z = Symbol('z') # z-coordinate
R = Symbol(r'\mathcal{R}') # the environment
p = Symbol('p') # a particle
V_p = _idx(V, p) # volume of a particle
r_p = _idx(r, p) # position of a particle
rho_p = _idx(abc.rho, p) # density of a particle
