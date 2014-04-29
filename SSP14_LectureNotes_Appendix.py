n = Symbol('n') # finite integer
x = MatrixSymbol('x', n, 1) # a random vector
mu = MatrixSymbol(r'\mu', n, 1)
E = Function('E') # expected value
C = MatrixSymbol('C', n, n) # covariance matrix
a_50_1 = Eq(mu, E(x))
a_50_2 = Eq(C, E((x - mu) * (x - mu).T))
