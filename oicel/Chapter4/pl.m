function u = pl(lambda)
% u = pl(lambda)
% solve the physical layer optimization problem
% for testing, rate region is a hypersphere 
%
% lambda: dual variables
%
% Output
%  u: arc capacities
if sum(lambda) == 0
  lambda = rand(size(lambda));
end
u = lambda/norm(lambda);
end

