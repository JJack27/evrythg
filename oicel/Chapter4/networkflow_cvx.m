
function [x, u, lambda, util] = networkflow_cvx(M,terminal,source) %#ok<STOUT>

[n_nodes, n_flows] = size(M); %#ok<NASGU>
n_com = length(terminal);

for com = 1:n_com
  c{com} = -M(terminal(com),:)'; %#ok<AGROW>
  Mbar{com} = M(setdiff(1:n_nodes,[terminal(com),source(com)]),:); %#ok<AGROW>
end

d = zeros(n_nodes-2,1);

cvx_begin quiet
  variable util(n_com)
  variable x(n_flows,n_com)
  variable u(n_flows)  
  dual variable lambda
  maximize (sum(util))
  subject to 
    for com = 1:n_com
      util(com) <= log(1 + c{com}'*x(:,com));  %#ok<NODEF,VUNUS>
      Mbar{com}*x(:,com) == d;  %#ok<EQEFF>
      x(:,com) >= 0;  %#ok<VUNUS>
    end
    lambda: sum(x, 2) <= u; %#ok<VUNUS>
    norm(u) <= 1; %#ok<VUNUS>
    u >= 0; %#ok<VUNUS>
cvx_end 

fprintf(1, ['The optimal value found with CVX is '...
    num2str(sum(u),'%1.4f') '\n']);
end
