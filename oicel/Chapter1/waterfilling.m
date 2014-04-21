function [R,p,mu] = waterfilling(h,s,P)
% function [R,p,mu] = waterfilling(h,s,P)
%
% Calculation of the optimal solution to the following sum rate
% maximization problem under a limited sum power budget.
%     R =    max sum(log2(1+|hi|^2/si*pi) 
%            s.t.:   pi >= 0   for all i
%                    sum(pi) <= P
% The solution is calculated via the waterfilling procedure.
%
% Inputs
% h: vector of channel coefficients h1,...,hn
% s: vector of noise variances sigma1^2,...,sigman^2
% P: available sum transmit power P
% Outputs
% R: value of the maximal sum rate R
% p: vector of optimal transmit powers p1,...,pn
% mu: value of th optimal Lagrangian multiplier mu
[g, idx] = sort(abs(h).^2 ./ s.^2, 'descend');
c = 1./g;
n = length(g);
w = @(k) (P + sum(c(1:k)))/k;
for k = 1:n-1
%fprintf('%d: %f <  %f <  %f\n', k, c(k),  w(k), c(k+1))
if c(k) > w(k) || isinf(w(k+1)); break; end
end
if c(k) > w(k); k = k-1; end
p = w(k) - c;
p(k+1:end) = 0;
R = sum(log2(1 + g .* p));
mu = 1/(log(2) * w(k));
i(idx) = 1:length(idx); % a trick to undo sorting
p = p(i);
end
