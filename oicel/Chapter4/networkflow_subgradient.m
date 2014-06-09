function [x, u, lambda, util, D] = ...
    networkflow_subgradient(M, terminal, source) %#ok<STOUT>
% function [x, u, lambda, util, D] = networkflow_subgradient(M, terminal, source)
%
% network flow maximization, dual decomposition, subgradient
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

% Initialize
[~, n_flows] = size(M);
C = length(terminal);
alpha = @(l) 1 / (l);
U = zeros(n_flows, C);

% Setup visualization
figure; hold all
xlabel('Iteration index $l$')
ylabel('Dual function value $D(\lambda_l)$', 'Interpreter', 'Latex')
colors = get(gca,'ColorOrder');

for c = 1:C
L = 10;
D = inf(L, 1);
lambda = ones(n_flows, 1);
for l = 1:L
    
    % network layer problem
    [s, x] = nl(M, terminal(c), source(c), lambda);
    
    % physical layer problem
    u = pl(lambda);
    
    % compute dual value
    D(l) = dualFunctionValue(s, lambda, u, x) ;
    
    scatter(l, D(l), [], colors(c, :)); drawnow
    % subgradient update cf. 140531164618
    lambda = max(lambda - alpha(l) * (u - x), 0);
    
    fprintf(1, ['Iteration: ' num2str(l,'%u')...
        '\t \t Best Dual: '  num2str(min(D(1:l)),'%1.2e')  '\n']);   
end
U(:, c) = u;
end

[x, util] = primal_recovery_template(U, M, terminal, source);


fprintf(1, '\n ===========================================================\n');
fprintf(1, ['Best Dual ' num2str(min(D), '%1.4f') '\t Primal ' num2str(sum(util),'%1.4f')  '\n']);
end


