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

  [n_nodes,n_flows] = size(M);  
  n_com = length(terminal);

  lambda = ones(n_flows,1);
  
  epsilon = 0.01;
  
  for iter = 1:1000

    % network layer problem
    [s,x] = nl(M,terminal,source,lambda);
    
    % physical layer problem
    u = pl(lambda);    
    
    % collect results
    S(iter) = s;  
    X(:,iter) = x;
    U(:,iter) = u;

    % compute dual value 
    D(iter) =   
    best_dual = min(D);

    % cutting plane master problem (hint: use S,X and U)
    lambda =    

    % update upper and lower bound
    LB(iter) = 
    UB(iter) = 
    
     
    % convergence criterion 
    criterion = 
    
    fprintf(1, ['Iteration: ' num2str(iter,'%u') '\t \t Lower Bound: '  num2str(LB(iter),'%1.4f') '\t \t Upper Bound: '  num2str(UB(iter),'%1.4f') '\t \t convergence criterion: '  num2str(criterion,'%1.4f') '\n']);
   
    if (criterion < epsilon )
      break
    end

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
        util(com) <= log(1 + c{com}'*x(:,com))
        Mbar{com}*x(:,com) == d 
        x(:,com) >= 0
      end
      sum(x,2) <= u
  cvx_end 

 
  fprintf(1, '\n ===========================================================\n');
  fprintf(1, ['Best Dual ' num2str(best_dual,'%1.4f') '\t Primal ' num2str(sum(util),'%1.4f')  '\n']);

end



