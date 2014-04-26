function [R,p,mu] = waterfilling_cvx(h,sigma,P)
% 140426090339
%function [R,p,mu] = waterfilling_cvx(h,sigma,P)
%
% Calculation of the optimal solution to the following sum rate
% maximization problem under a limited sum power budget.
%     R =    max sum(log2(1+|h_i|^2/sigma_i*pi) 
%            s.t.:   pi >= 0   for all i
%                    sum(pi) <= P
% The solution is calculated via CVX.
%
% Inputs
% h: vector of channel coefficients h1,...,hn
% sigma: vector of noise variances sigma1^2,...,sigman^2
% P: available sum transmit power P
% Outputs
% R: value of the maximal sum rate R
% p: vector of optimal transmit powers p1,...,pn
% mu: value of th optimal Lagrangian multiplier mu

h = h(:);
sigma = sigma(:);
gamma = (abs(h) .^ 2 ) ./ (sigma .^2);
% determine n
n = length(h); %#ok<NASGU>
%#ok<*NOPRT>
cvx_begin 
	cvx_quiet true % no screen outpunt
    cvx_solver SDPT3 % select solver
    variable p(n)
    maximize(sum_log(1 + gamma .* p))
    subject to
		sum(p) <= P
        p >= 0 
cvx_end
R = cvx_optval/log(2);
[p_, i] = max(p);
assert(p_ > 0)
mu = 1/(p_ + 1/gamma(i))/log(2);
%{
figure
hold
h = [plot(p/50, 'b'), plot(gamma, 'g')]
legend({'$p/50$', '$\gamma$'}, 'Interpreter', 'Latex')
%}
end
