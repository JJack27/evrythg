%% NOAD Assignment 2 - Task 2
% Matrix inversion interpreted as optimization problem
% i.e. $\min\limits_X (||A*X-I||_{F}^{2})$

% Initializ A
A = [2, 3, 0, 1;
     0, 7, 3, 0;
     1, 3, 1, 1;
     1, 1, 0, 1];
 n = size(A, 1);
 %% Parameters
 c = 0.8;
 eps = 1e-2 % termination threshold
 %% Gradient descent
 % Initialize X
 I_n = eye(n);
 X = eye(n);
 % $f(x) = min(||A*X-I||_F^2) = tr((AX - I) (AX - I)^T)$
 % $\nabla f(x) = 2 A^T A X - A^T$
 g = @(X) 2 * A' * (A * X - I_n); 
 h = @(X) X / norm(X);
 f = @(X) norm(A * X - I_n, 'fro')^2;
%% Iterate gradient descent
alpha = 1;
while true % alternative termination condition abs(f(X)) > 1e-6 % !!! Takes a while !!!
    H = - h(g(X));
    alpha = alpha / 0.9;
    % Armijo condition
    while  f(X + alpha * H) >= f(X) + alpha * c * trace(H * X')  
        alpha = alpha * 0.9; 
     end   
    X = X +  alpha * H; 
    if norm(alpha * H) < eps; break; end
    % f(X)
    % norm(alpha * H)
end
%% Compare results
X
A \ eye(n)
 