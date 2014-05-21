function [x, val] = projGrad(fun, grad, proj, x, N, method)
if ~exist('method','var'); method = 'fixed'; end % default parameter handling
zeta = 1e-10;
xOld = x;

switch method
    case 'optimal'
        options = optimset('Display','off', ...
            'LargeScale','off');
    case 'armijo'
        beta  = 0.5;
        sigma = 0.2;
end

val = zeros(N, 1);
s   = 100;
fnorm2 = @(X) X(:)' * X(:);
for a = 1:N
    switch method
        case 'optimal'
            s = fminunc(@(s)- fun(proj(xOld + s * grad(xOld))), 1, options);
        case 'open_loop'
            s = 1/a;
        case 'armijo'
            b = 0; 
            s = 2 * s;
            c = @(b) sigma * fnorm2(proj(xOld + s * beta^b * grad(xOld)) - xOld) / (s * beta^b);
            while true
                if fun(proj(xOld + s * beta^b * grad(xOld))) - fun(xOld) > c(b+1)
                    break;
                end
                b = b+1;
            end
            s = s * beta^b;
        otherwise
            s = 1;
    end
    x = proj(x + s * grad(xOld));
    gApprox = (x - xOld)/s;
    if fnorm2(gApprox) < zeta; break; end
    val(a) = fun(x);
end
end