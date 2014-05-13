%% Gradient descent method 
% Solve 
% $f(x) = x^T A x - b^T x$
A = [ 5, 2;  2, 3]
b = [-2; 4]
g = @(x) 2 * A * x - b
alpha = @(x) g(x)' * g(x) / (2 * g(x)' * A * g(x))
%% Initial value
x = [5; 2]
%% Iterate
x = x - alpha(x) * g(x)
