function [R,s,mu] = worstCaseRate(p,N)
% Function: [R,s,mu] = worstcaseRate(p,N)
%
% Calculation of the worst case rate to the sum rate 
% minimization problem under a limited sum noise power.
%     R =    min sum(log2(1+psi_i/sigma_i) 
%            s.t.:   sigma_i >= 0   for all i
%                    sum(sigma_i) <= N
% The sulution tried to be calculated via CVX.
% Note that the psi_i has to be strictly positive.
%
% Inputs
% p: vector of useful received power psi_1,...,psi_m
% N: available sum noise power N
%
% Outputs
% R: value of the worst-case sum rate R
% s: vector of worst-case powers sigma_1,...,sigma_m
% mu: value of the optimal Lagrangian multiplier mu
