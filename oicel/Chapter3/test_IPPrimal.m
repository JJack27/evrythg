T = 10;
zeta = 1e-2;
err = zeros(T,1);
ok = true;
clc

for t = 1:T
    fprintf('Iteration # %d\t', t)
    m = 200;
    n = 400;
        
    % Optimal solutions
    x = rand(n,1);
    s = rand(n,1);
    I = rand(n,1)>0.5;
    x( I) = 0;
    s(~I) = 0;
    
    y = randn(m,1);
    
    % Parameters
    A = randn(m,n);
    c = s + A'*y;
    b = A*x;
    beta = 0.75;
    %{
    % for comparison
    [x_, u_, v_] = linprog_cvx(c, A, b)
    figure; hold all;
    plot(x,  'o')
    plot(x_, 'o')
    %}
    [xh, yh] = IPPrimal(c, A, b, beta, 1, 1e-6);
    
    sh = max(0,c - A'*yh);
    
    rd = A'*yh + sh - c;
    rp = A*xh - b; % residual in the primal equality constraint
    rs = xh.*sh;
    
    err = max([max(abs(rd)),...
        max(abs(rp)),...
        max(abs(rs))] );
    fprintf('max(err) = %f\n', err)
    if err > zeta
        fprintf('\t !!! Error exceeds %f !!!\n', zeta)
        % keyboard
        ok = false;
    end
    err(t) = err;
end

if ok
    fprintf('\t\t\t\t Passed all tests.\n')
end
