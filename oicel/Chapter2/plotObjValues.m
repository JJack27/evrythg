function plotObjValues(H, P, I)
K = size(H,3);
n = size(H,2);
% W0 = rand(n,n,K)/10; %\todo{Breaks the armijo rule'}
for k = 1:K
    W0(:,:,k) = eye(n); %#ok<AGROW>
    Q0(:,:,k) = eye(n); %#ok<AGROW,NASGU>
end
methods = {'fixed', 'open loop', 'armijo', 'optimal'};
handles = zeros(size(methods));
for m = 1:length(methods)
tic;
N = 5; % number of successive steps;
val = zeros(I*N+1, 1);
ix = 2:N+1;
x = W0;
fun = @(x) rateW(x, H);
val(1) = fun(x);
for i = 1:I
[x, val(ix)] = projGrad(fun,...
    @(x) gradW(x, H),  @(x) projW(x, P), x, N, strrep(methods{m},' ', '_'));
ix = ix + N;
end
fprintf('Testing %s stepsize:\n', upper(methods{m}))
toc;
handles(m) = plot(1:length(val), val, 'LineWidth', 2);
end
legend(handles, methods)
title('Comparing step sizes s(a)')
xlabel('Iteration index a')
ylabel('Objective value')
grid()
end