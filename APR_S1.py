from numpy import array
from numpy import dot
from numpy import ones
from numpy import arange
from numpy.linalg import inv
Phi = array([ones(5), arange(5) + 1]).T
Y = array([1, 3, 3, 6, 7]).T
P_ = inv(dot(Phi.T, Phi))

# cf. 140426154601
tH_ = dot(dot(P_, Phi.T), Y)


# cf. 140426154206
phi = array([[1], [6]])
y = array([7])
K = dot(dot(P_,  phi), inv(1 + dot(dot(phi.T, P_) , phi)))
tH = tH_ + dot(K, y - dot(phi.T , tH_))
