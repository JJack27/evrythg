function [x y s] = IPPrimalDual(c, A, b, sigma, zeta)
% function [x y s] = IPPrimalDual(c,A,b,sigma,zeta)
%
% Linar Program solver using a primal-dual method.
%
% Inputs
% c,A,b: problem data which defines the linear program in standard form
% sigma: optional parameter defining the centering parameter (default: sigma = 0.5)
% zeta: optional parameter controlling the termination of the algorithm (default: zeta = 0.0001)
%
% Outputs
% x,y,s: resulting estimates of the optimal primal and dual variables
m = size(A, 1);
n = size(A, 2);
x = ones (n, 1);
y = zeros(m, 1);
s = ones (n, 1);
e_n = ones(n, 1);
while true
d = s' * x
if d < zeta; break; end
mu = d / n;
X = diag(x);
S_ = diag(1./s); 
D_ = (A * S_* X * A') \ eye(m);
r_c = A' * y + s - c; 
r_d = -b + A * S_ * (e_n * mu + X * r_c);
d_y = D_ * r_d;
d_s = -r_c + A' * d_y;
d_x = S_ * (sigma * mu * e_n - X * diag(s) * e_n -X * d_s);
i = d_x < 0;
j = d_s < 0;
alpha = .99995 * min([min([min(x(i) ./ -d_x(i)), min(s(j) ./ -d_s(j))]), 1]);
x = x + alpha * d_x;
y = y + alpha * d_y;
s = s + alpha * d_s;
end
end
