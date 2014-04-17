from sympy.physics.units import *
from sympy import Symbol
from sympy import Derivative
from sympy import Function

# Cartesian unit vectors
i = Symbol(r'\mathbf{i}') # unit vector along x-Axis
j = Symbol(r'\mathbf{j}') # unit vector along y-Axis
k = Symbol(r'\mathbf{k}', commutative=False) # unit vector along z-Axis
V = Symbol(r'\mathcal{V}') # Volume
Vi = Symbol(r'\operatorname{d}%s' %(V)) # infinitesimal  volume
D = Symbol(r'\mathcal{D}') # Volume of displaced water
Di = Symbol(r'\operatorname{d}%s' %(D)) # infinitesimal  volume
rho = Symbol(r'\rho') # mass density
rho_W = Symbol(r'\rho_W') # mass density of water
rhoi = Symbol(r'\operatorname{d}%s' %(rho)) # infinitesimal mass density
M = Symbol(r'M') # mass
W = Symbol(r'W') # gravity force
B = Symbol(r'B') # buoyant force
C_W = Symbol(r'C_W') # center of gravity 
C_B = Symbol(r'C_B') # center of buoyancy
X = Symbol(r'X') # unknown force
F = Symbol(r'F') # total force
Wi = Symbol(r'\operatorname{d} %s' %(W)) # infinitesimal forces
Mi = Symbol(r'\operatorname{d} %s' %(m)) # infinitesimal masses
g = Symbol(r'g') # earth acceleration
s = Symbol(r's') # state vector
sdot = Derivative(s, Symbol('t'))
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
