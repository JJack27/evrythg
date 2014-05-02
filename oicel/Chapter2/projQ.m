function QP = projQ(Q, P)
r = size(Q,1);
K = size(Q,3);
if sum(arrayfun(@(k) trace(Q(:, :, k)), ... % no projection necessary
        1:K)) < P; QP = Q; return; end
Q_ = arrayfun(@(k) Q(:,:,k), 1:K, 'UniformOutput', false); 
[U, Lambda] = eig(blkdiag(Q_{:}));
L = size(Q, 1) * K;
[lambda, i] = sort(diag(Lambda), 'descend');
U = U(:, i); % reorder colums for consistency 
for l = L:-1:1
    if l * lambda(l) - sum(lambda(1:l)) + P > 0; break; end
end
mu = 1/l * (sum(lambda(1:l)) - P);
D = diag(max(lambda - mu, 0));
C = U * D * U';
% build an indicator matrix to retrieve the $Q_i^{(a)}$
I_ = arrayfun(@(k) true(size(Q(:,:,k))), 1:K, 'UniformOutput', false);
QP = reshape(C(blkdiag(I_{:})>0),r, r, K);
end