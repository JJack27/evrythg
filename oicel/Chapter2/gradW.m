function g = gradW(W, H)
K = size(W, 3);
m = size(H, 1);
X = arrayfun(@(l) H(:, :, l) * W(:, :, l) * W(:, :, l)' * H(:, :, l)', ...
    1:K, 'UniformOutput', false);
% inversion via backslash, compute only once
X_ = (eye(m) + sum(cat(3, X{:}),3)) \ eye(m);
g = reshape(cell2mat(arrayfun(@(k) H(:, :, k)' * X_ * H(:, :, k) * W(:, :, k), ...
    1:K, 'UniformOutput', false))/log(2), size(W));
end