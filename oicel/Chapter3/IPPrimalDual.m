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

function [x y s] = IPPrimalDual(c, A, b, sigma, zeta)
