function R = rateW(W,H)
K = size(W,3);
S = arrayfun( @(k) W(:, :, k) * W(:, :, k)', ...
    1:K, 'UniformOutput', false);
R = rateQ(cat(3, S{:}),H); % code reuse 
end
