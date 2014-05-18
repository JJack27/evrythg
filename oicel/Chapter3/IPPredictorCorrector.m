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


function [x y s] = IPPredictorCorrector(c,A,b,zeta)
