noTests = 10;

zeta = 1e-2;
err = zeros(noTests,1);

ok = true;
%{ 
% A small scale testcase
% A = [2, 1, 1, 0;
%      1, 2, 0, 1];
% b = [8, 6]';
% c = [2, 3, 0, 0]';
% [xh, yh, sh] = IPPrimalDual(c,A,b,0.5,0.001)

% [xh, yh, sh] = linprog_cvx(c,A,b);
IPPrimal(c, A, b)
% Another textbook example
A = [1, 2]
c = [3; -1]
b = 2;
% [xh, yh, sh] = linprog_cvx(c,A,b);
% [xh, yh, sh] = IPPrimalDual(c,A,b,0.5,0.01);
[xh, yh, sh] = IPPredictorCorrector(c,A,b,1e-4);
%}

for t = 1:noTests
    fprintf('Test #%d: \n', t)
    tic
    
    m = 200;
    n = 400;
    
    %optimal solutions
    x = rand(n,1);
    s = rand(n,1);
    I = rand(n,1)>0.5;
    x(I) = 0;
    s(~I) = 0;
    
    y = randn(m,1);
    
    %parameters
    A = randn(m,n);
    c = s + A'*y;
    b = A*x;
    
    % different methods
%      [xh, yh, sh] = linprog_cvx(c, A, b);
%      [xh, yh, sh] = IPPrimalDual(c, A, b, 0.5, 0.001);
     [xh, yh, sh] = IPPredictorCorrector(c, A, b, 1e-6);
    
    [r_b, r_c, r_s] = residuals(c, A, b, x, s, y);
    err(t) = max([max(abs(r_b)), max(abs(r_c)), max(abs(r_s))]);
    if err(t) > zeta
        keyboard
        ok = false;
    end
    toc
end

if ok
    display('All passed')
end
