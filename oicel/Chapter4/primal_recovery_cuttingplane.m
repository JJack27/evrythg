% [x,u,util] = primal_recovery_cuttingplane(X,U,S,alpha)
%
% Compute general primal recovery
%
% Input:
%  X: primal flow variables over iterations
%  U: primal capacity variables over iterations
%  S: primal 's' values over iterations
%  alpha: dual variables of cutting plane master problem
%
% Output:
%  x: feasible flow variables
%  u: feasible capacity variables
%  util: utility function value
%
function [x,u,util] = primal_recovery_cuttingplane(X,U,S,alpha)
