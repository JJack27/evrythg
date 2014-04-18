function [R,p,mu] = waterfilling(h,s,P)
% function [R,p,mu] = waterfilling(h,s,P)
%
% Calculation of the optimal solution to the following sum rate
% maximization problem under a limited sum power budget.
%     R =    max sum(log2(1+|hi|^2/si*pi) 
%            s.t.:   pi >= 0   for all i
%                    sum(pi) <= P
% The sulution is calculated via the waterfilling procedure.
%
% Inputs
% h: vecotr of channel coefficients h1,...,hn
% s: vecotr of noise variances sigma1^2,...,sigman^2
% P: available sum transmit power P
% Outputs
% R: value of the maximal sum rate R
% p: vector of optimal transmit powers p1,...,pn
% mu: value of th optimal Lagrangian multiplier mu
