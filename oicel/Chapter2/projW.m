function WP = projW(W, P)
WP = sqrt(P/sum(arrayfun(@(k) norm(W(:,:,k), 'fro')^2,...
    1:size(W,3)))) * W;
end
