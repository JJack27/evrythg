function [x, u, lambda, util, D, LB, UB] = networkflow_cuttingplane(M, terminal, source)
% [x,u,lambda,util,D,LB,UB] = networkflow_cuttingplane(M,terminal,source)
% Solve network flow problem with cutting plane method
%
% Input
%  M: node-arc incidence matrix
%  terminal: index of the terminal
%  source: index of the source
%
% Output
%
% x: flow solution
% u: capacity solution
% lambda: dual variables
% util: utility function value
% D: dual function value over iterations
% LB: lower bounds over iterations for utility function
% UB: upper bounds over iterations for utility function

[n_nodes, n_flows] = size(M);
n_com = length(terminal);
lambda = ones(n_flows,1);
epsilon = 0.01;

% allocate variables
L = 1000;
S = zeros(1, L);
D = zeros(1, L);
U = zeros(n_flows, L);
X = zeros(n_flows, L);
LB = zeros(1, L);
UB = zeros(1, L);


for l = 1:L
    
    % solve subproblems cf. 140531160015
    % network layer subproblem
    [s, x] = nl(M, terminal, source, lambda);
    % physical layer subproblem
    u = pl(lambda);
    
    % collect results
    S(l) = s;
    X(:, l) = x;
    U(:, l) = u;
    
    % compute dual value
    D(l) = dualFunctionValue(s, lambda, u, x);
    
    % solve the master problem
    cvx_begin quiet
    variable lambda(n_flows);
    variable r(1)
    minimize r;
    subject to
    for k = 1:l
        lambda >= 0 %#ok<NOPRT>
        r >= log(1 + S(k)) + lambda' * (U(:, k) - X(:, k)); %#ok<VUNUS>
    end
    cvx_end
    
    % update upper and lower bound
    LB(l) = r;
    UB(l) = min(D(1:l)); % $\min\limits_{1 \leq k \leq l}d_k^*$
    
    
    % convergence criterion
    criterion = (min(UB(1:l)) - r) / abs(r);
    
    fprintf(['Iteration: ' num2str(l,'%u') '\t \t Lower Bound: '...
        num2str(LB(l),'%1.4f') '\t \t Upper Bound: '  num2str(UB(l),'%1.4f')...
        '\t \t convergence criterion: '  num2str(criterion,'%1.4f') '\n']);
     if (criterion < epsilon ); break; end 
end
[~, i] = min(D(1:l));
u = U(:, i);
% Recover optimal primal values
for com = 1:n_com
    c{com} = -M(terminal(com),:)'; %#ok<AGROW>
    Mbar{com} = M(setdiff(1:n_nodes,[terminal(com),source(com)]),:); %#ok<AGROW>
end
d = zeros(n_nodes-2, 1);
cvx_begin quiet
variable util(n_com)
variable x(n_flows,n_com)
maximize (sum(util))
subject to
for com = 1:n_com
    util(com) <= log(1 + c{com}'*x(:,com)); %#ok<VUNUS>
    Mbar{com}*x(:,com) == d; %#ok<EQEFF>
    x(:,com) >= 0; %#ok<VUNUS>
end
sum(x,2) <= u; %#ok<VUNUS>
cvx_end


fprintf(1, '\n ===========================================================\n');
fprintf(1, ['Best Dual ' num2str(min(D(1:l)),'%1.4f')...
    '\t Primal ' num2str(sum(util),'%1.4f')  '\n']);

end



