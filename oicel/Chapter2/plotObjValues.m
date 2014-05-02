function plotObjValues(H, P, I)
K = size(H,3);
n = size(H,1);
% W0 = rand(n,n,K)/10; %\todo{Breaks the armijo rule'}
for k = 1:K
    W0(:,:,k) = eye(n); %#ok<AGROW>
    Q0(:,:,k) = eye(n); %#ok<AGROW,NASGU>
end
methods = {'fixed', 'open loop', 'armijo', 'optimal'};
handles = zeros(size(methods));
for m = 1:length(methods)
val = zeros(1, I);
x = W0;
fun = @(x) rateW(x, H);
val(1) = fun(x);
tic;
for i = 2:I
[x, val(i)] = projGrad(fun,...
    @(x) gradW(x, H),  @(x) projW(x, P), x, 1, strrep(methods{m},' ', '_'));
end
fprintf('Testing %s stepsize:\n', upper(methods{m}))
toc;
handles(m) = plot(1:I, val, 'LineWidth', 2);
end
legend(handles, methods)
title('Comparing step sizes s(a)')
xlabel('Iteration index a')
ylabel('Objective value')
end