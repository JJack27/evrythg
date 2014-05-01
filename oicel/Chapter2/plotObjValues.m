function plotObjValues(H,P,nIter)

K = size(H,3);
N = size(H,1);

W0 = zeros(N,N,K);
Q0 = zeros(N,N,K);

for k = 1:K
    W0(:,:,k) = eye(N);
    Q0(:,:,k) = eye(N);
end

%TODO
