T = 10;
zeta = 1e-2;
err = zeros(T,1);
ok = true;
clc

for t = 1:T
    fprintf('Test # %d\t', t)
    tic
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
    
    [r_p, r_d, r_s] = residuals(c, A, b, x, s, y);
    
    err(t) = max([max(abs(r_d)),...
        max(abs(r_p)),...
        max(abs(r_s))] );
    fprintf('max(err) = %f\n', err(t))
    if err(t) > zeta
        fprintf('\t !!! Error exceeds %f !!!\n', zeta)
        % keyboard
        ok = false;
    end
    toc
end

if ok
    fprintf('\t\t\t\t Passed all tests.\n')
end
