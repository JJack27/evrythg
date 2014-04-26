function [R, sigma, mu] = worstCaseRate(psi, N)
% Function: [R, s, mu] = worstcaseRate(p, N)
%
% Calculation of the worst case rate to the sum rate 
% minimization problem under a limited sum noise power.
%     R =    min sum(log2(1+psi_i/sigma_i) 
%            s.t.:   sigma_i >= 0   for all i
%                    sum(sigma_i) <= N
% The sulution tried to be calculated via CVX.
% Note that the psi_i have to be strictly positive.
%
% Inputs
% psi: vector of useful received power psi_1,...,psi_m
% N: available sum noise power N
%
% Outputs
% R: value of the worst-case sum rate R
% s: vector of worst-case powers sigma_1,...,sigma_m
% mu: value of the optimal Lagrangian multiplier mu
if~(all(psi > 0)); psi(psi<0) = 0+eps; end
mu_ = @(m)2 * N + sum(psi) - sum(sqrt(psi .^ 2 + 4 * psi * m));
mu_dash = fzero(mu_,...
[0,((2 * N + sum(psi)) ^ 2 - sum(psi .^ 2)) / sum(psi)]... % search intervall
);
sigma = -psi/2 + 0.5 * sqrt(psi.^2 + 4 * psi * mu_dash);
R = sum(log2(1 + psi ./ sigma));
mu = 1/(mu_dash * log(2));
end