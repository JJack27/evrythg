n = Symbol('n') # finite dimensionality
x = MatrixSymbol('x', n, 1) # a jointly gaussian random vector
mu_x = MatrixSymbol(r'mu_x', n, 1) # mean vector
sigma_x = Symbol(r'sigma_x') # standard deviation
C_x = MatrixSymbol(r'C_x', n, n) # covariance matrix 
A = MatrixSymbol('A', n, n) # a deterministic matrix
b = MatrixSymbol('b', n, 1) # a deterministic vector
def normal(mu, sigma):
	"""
	Normal distribution
	"""
	return Function(r'\mathcal{N}')(mu, sigma**2)
def mv_normal(mu, C):
	"""
	Multivariate normal distribution
	"""
	return Function(r'\mathcal{N}')(mu, C)
def aft(A, x, b):
	""" 
	An affine Transformation
	"""
	return A * x + b 
aft(A, x, b) \sim mv_normal(A * mu_x, A * C_x * A.T)



