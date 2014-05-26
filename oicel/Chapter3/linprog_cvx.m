function [x, y, s] = linprog_cvx(c, A, b) %#ok<STOUT>
n = size(A,2); %#ok<NASGU>
cvx_begin
    variable x(n);
    dual variable y;
    dual variable s;
    minimize(c' * x);
    subject to
    	cvx_quiet true % no screen outpunt
        s : -x <= 0; %#ok<*VUNUS>   % dual variable $u$ associated to the inequality constraint
        y : A * x == b; %#ok<EQEFF> % dual variable $v$ associated to the   equality constraint
cvx_end
end
