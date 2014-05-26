%% Import and preprocessing
C = importLogs('C:\Users\Martin\Surfbrett\messdaten\2014_05_23_11_47_42.csv');
t = datenum(C(:,1), 'yyyy_mm_dd_HH_MM_SS.FFF');
t_ = (t - min(t)) * 24 * 3600; % relative time in seconds
% D = sortrows([t_, cell2mat(C(:, 2:end))]); % assume that only writing swaps timestamps
D = [t_, cell2mat(C(:, 2:end))];
% assert(all(diff(D(:,1)) >= 0))
g = mean(D(D(:,2) == 6, 3));
D(:, 3) = D(:,3) / g * 9.81;
%% Show Timing problmes
figure
i = D(:,2) == 4;
t = D(i, 1);
a_x = D(i, 3);
%{
figure
title(sprintf('Timing problems \n(i.e  at t ~ 240[s])'))
plot(t, a_x)
%}
%% Filtering, interpolation for constant sampling rate etc.
[t, i] = unique(t);
k = t(1) : 0.1 : t(end);
figure; hold all
legend([plot(t, a_x(i)),...
plot(decimate(k, 10),...
    decimate(interp1(t, a_x(i), k), 10), ...
'LineWidth', 3)], {'Raw measurements', 'Decimated'})
xlabel('t_{rel} [s]')
ylabel('a_x [m/s^2]')
%% Ingegration
% W = D(D(:, 1) > 0 & D(:, 1) < 180, :);
% i_x = W(:,2) == 4;
% i_y = W(:,2) == 5;
% i_z = W(:,2) == 6;
% int = @(XY) [XY(1:end-1,1), cumsum(XY(1:end - 1, 2) .* diff(XY(:,1)))];
% II  = int(int([W(i_x, 1), W(i_x, 3)]));
% figure
% plot(II(:, 1), II(:, 2)) 
% figure
% plot(W(i_x, 1), W(i_x, 3))