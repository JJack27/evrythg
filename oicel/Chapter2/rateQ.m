function R = rateQ(Q, H)
K = size(Q,3);
S = arrayfun(@(k) H(:, :, k) * Q(:, :, k) * H(:, :, k)', ...
    1:K, 'UniformOutput', false);
R = real(log2(det(eye(size(H,1)) + sum(cat(3, S{:}),3) )));
end
