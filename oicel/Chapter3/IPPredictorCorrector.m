function [x, y, s] = IPPredictorCorrector(c, A, b, zeta)
% function [x y s] = IPPredictorCorrector(c,A,b,zeta)
%
% Linar Program solver using a primal-dual predictor-corrector interior point method.
%
% Inputs
% c,A,b: problem data which defines the linear program in standard form
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
while true
    d = s' * x; % duality gap
    if d < zeta; break; end
    mu = d / n;
    X =  diag(x);
    S = diag(s);
    A_ = [zeros(n), A'         , eye(n);
        A       , zeros(m, m+n);
        S       , zeros(n, m),      X];
    
    [r_b, r_c, r_s] = residuals(c, A, b, x, s, y);
    d_a = A_ \ (-1 * [r_c; r_b; r_s]); %[ _cf('140525141041') ]
    d_x = d_a(1:n);
    d_s = d_a(n+m + 1:end);
    sigma = (((x + alpha_(x, d_x) * d_x)' * (s + alpha_(s, d_s) * d_s) / n) / mu)^3;
    d_c = A_ \ [zeros(n, 1); zeros(m, 1); sigma * mu * e_n - d_a(1:n) .* d_a(n+m + 1:end)];
    
    d_  = d_a + d_c;
    d_x = d_(        1 : n    );
    d_y = d_(    n + 1 : n + m);
    d_s = d_(m + n + 1 : end  );
    
    a_p = alpha_(x, d_x);
    a_d = alpha_(s, d_s);
    alpha = gamma * min(min(a_p,  a_d), 1);
    
    
    x = x +  alpha * d_x;
    s = s +  alpha * d_s;
    y = y +  alpha * d_y;
end
end

