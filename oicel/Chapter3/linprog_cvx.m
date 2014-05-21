function [x, u, v] = linprog_cvx(c, A, b) %#ok<STOUT>
n = size(A,2); %#ok<NASGU>
cvx_begin
    variable x(n);
    dual variable u;
    dual variable v;
    minimize(c' * x);
    subject to
    	cvx_quiet true % no screen outpunt
        u : -x <= 0; %#ok<*VUNUS>   % dual variable associated to the inequality constraint
        v : A * x == b; %#ok<EQEFF> % dual variable associated to the   equality constraint
cvx_end
end
