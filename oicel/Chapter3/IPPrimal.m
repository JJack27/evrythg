function [x, y] = IPPrimal(c, A, b, beta, tau, zeta)
% function [x y] = IPPrimal(c,A,b,beta,tau,zeta)
%
% Linar Program solver using a primal method.
%
% Inputs
% c,A,b: problem data which defines the linear program in standard form
% beta: optional parameter that controls the progression of the algorithm (default: beta = 0.5)
% tau: optional parameter defining a starting value for tau (default: tau = 1)
% zeta: optional parameter controlling the termination of the algorithm (default: zeta = 0.0001)
%
% Outputs
% x,y: resulting estimates of the optimal primal and dual variables
if ~exist('beta','var'); beta = 0.5; end % default parameter handling
if ~exist('tau','var');  tau  = 1.0; end
if ~exist('zeta','var'); zeta = 1e-4; end
m = size(A, 1);
n = size(A, 2);
x = ones (n, 1);
y = zeros(m, 1);
while true
    if tau < zeta; break; end
    X_ = diag(( 1./x ));
    A_ = [-tau * diag(diag(X_).^2) , A'   ;
        A                       , zeros(m)];
    b_ = [c - A' * y - tau * X_ * ones(n, 1);
          b - A * x];
    delta = A_ \ b_; % solve (3.6) via Backslash
    j = delta(1:n) < 0;
    alpha = .99995 * min(min(x(j) ./ - delta(j)), 1);
    x = x + alpha * delta(1:n);
    y = y + alpha * delta(n+1:end);
    tau = tau * beta;
    % c' * x - tau * sum(log(x)) % evaluate cost function
end
end




