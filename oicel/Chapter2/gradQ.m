function g = gradQ(Q, H)
K = size(Q,3);
m = size(H,1);
X = arrayfun(@(l) H(:, :, l) * Q(:, :, l) * H(:, :, l)', ...
    1:K, 'UniformOutput', false);
% inversion via backslash, compute only once
X_ = (eye(m) + sum(cat(3, X{:}),3)) \ eye(m);
g = reshape(cell2mat(arrayfun(@(k) H(:, :, k)' * X_ * H(:, :, k), ...
    1:K, 'UniformOutput', false))/log(2), size(Q));
end