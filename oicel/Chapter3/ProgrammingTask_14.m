%Programming Task 3.14

close all;

%Initialization
load 'IPNetworks.mat';

P0 = 1000;
N0 = 1;
n = 7;
dmax = 5;
alpha = 2:.5:6;

u = []; % vector that contains the capacity constraints
%% Create network incident matrix
% scatter(IPWN(n).x, IPWN(n).y) 
[i, j] = find(IPWN(n).distance <= dmax);
N = size(IPWN(n).distance, 1);
M = cell2mat(arrayfun(@(i, j) link(i, j, N), i, j, 'UniformOutput', false)');
assert(rank(M) == N - 1)