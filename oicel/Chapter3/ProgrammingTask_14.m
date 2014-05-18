%Programming Task 3.14

close all;

%Initialization
load 'IPNetworks.mat';

P0 = 1000;
N0 = 1;

dmax = 5;
alpha = 2:.5:6;

M = []; %network incident matrix
u = []; %vector that contains the capacity constraints

%TODO
