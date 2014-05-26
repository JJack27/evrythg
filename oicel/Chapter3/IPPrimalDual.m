function [x, y, s] = IPPrimalDual(c, A, b, sigma, zeta)
% function [x, y, s] = IPPrimalDual(c, A, b, sigma, zeta)
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
y = ones(m, 1);
s = ones (n, 1);
e_n = ones(n, 1);
gamma = 0.995;
%       [xh, yh, sh] = linprog_cvx(c,A,b)
while true
    d = s' * x; % duality gap
    if d < zeta; break; end
    mu = d / n;
    
    X =  diag(x);
    S_ = diag(1./s);
    [r_b, r_c, r_s] = residuals(c, A, b, x, s, y);
    
    r_d = - (A * S_) * (X * r_c + (sigma * mu - r_s)) - r_b;
    D_ = (A * S_* X * A') \ eye(m);
   
    d_y = D_ * r_d;
    d_s = - r_c - A' * d_y;
    d_x = S_ * (sigma * mu * e_n - r_s - X * d_s);
    
    a_p = alpha_(x, d_x);
    a_d = alpha_(s, d_s);
    alpha = gamma * min(min(a_p,  a_d), 1);
    
    x = x + alpha * d_x;
    y = y + alpha * d_y;
    s = s + alpha * d_s;

end
end
