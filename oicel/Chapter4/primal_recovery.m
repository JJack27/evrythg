% [alpha,x,u,util] = primal_recovery(X,U,S)
%
% Compute general primal recovery
%
% Input:
%  X: primal flow variables over iterations
%  U: primal capacity variables over iterations
%  S: primal 's' values over iterations
%
% Output:
%  alpha: coefficients of the optimal convex combination
%  x: feasible flow variables
%  u: feasible capacity variables
%  util: utility function value
%
function [alpha,x,u,util] = primal_recovery(X,U,S)
