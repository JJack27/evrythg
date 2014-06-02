function [x, u, lambda, util, D] = networkflow_subgradient(M, terminal, source)
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
  [n_nodes,n_flows] = size(M);
  n_com = length(terminal);
  alpha = @(l) 1 / (l);
  lambda = ones(n_flows, 1);
  L = 300;
  D = inf(L, 1);
  for l = 1:300

    % network layer problem
    [s, x] = nl(M, terminal, source, lambda);

    % physical layer problem
    u = pl(lambda);

    % compute dual value 
    D(l) = log(1 + s);
    scatter(l, D(l)); drawnow

    % subgradient update [ _cf('140531164618') ]
    lambda = max(lambda - alpha(l) * (u - x), 0); 
    
%     fprintf(1, ['Iteration: ' num2str(l,'%u') '\t \t Best Dual: '  num2str(best_dual,'%1.2e')  '\n']);

  end

  % Recover optimal primal values 

  for com = 1:n_com
    c{com} = -M(terminal(com),:)';
    Mbar{com} = M(setdiff(1:n_nodes,[terminal(com),source(com)]),:);
  end
  d = zeros(n_nodes-2,1);
  cvx_begin quiet
    variable util(n_com)
    variable x(n_flows,n_com)
    maximize (  sum(util)  )
    subject to 
      for com = 1:n_com
        util(com) <= log(1 + c{com}'*x(:,com));  %#ok<VUNUS>
        Mbar{com}*x(:,com) == d; %#ok<EQEFF>
        x(:,com) >= 0; %#ok<VUNUS>
      end
      sum(x,2) <= u; %#ok<VUNUS>
  cvx_end 

 
  fprintf(1, '\n ===========================================================\n');
  fprintf(1, ['Best Dual ' num2str(min(D), '%1.4f') '\t Primal ' num2str(sum(util),'%1.4f')  '\n']);
end


