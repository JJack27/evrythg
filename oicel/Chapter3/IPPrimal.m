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


function [x y] = IPPrimal(c,A,b, beta, tau, zeta)


