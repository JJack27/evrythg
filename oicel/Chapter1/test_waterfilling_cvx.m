function test_waterfilling_cvx(filename)

if nargin<1, filename = 'testData'; end

load(filename)

zeta = 1e-2;

ok = true;
disp('Testing waterfilling_cvx')
try
    for t=[1,2,4] %Not testing the cvx solution with the biggest system.
        for i=1:length(testSetsWF(t).P)
            % TODO What's the matter with test 2.3 ?
            %     for t=[2] 
            %        for i=3
            % Seems like I should not assign any power to c_1?
            fprintf('Running test %d.%d\n', t, i)
            [R,p,mu] = waterfilling_cvx(testSetsWF(t).h,testSetsWF(t).s,testSetsWF(t).P(i));
            if max(abs(testSetsWF(t).R(i)-R))>zeta
                display(['FAIL, wrong rate, test No. ' num2str(t) ', with P idx' num2str(i)])
                fprintf('Should be: %f  \t is \t %f \n', testSetsWF(t).R(i), R)
                ok=false;
            end
            if max(abs(testSetsWF(t).p(:,i)-p))>zeta
                display(['FAIL, wrong powers, test No. ' num2str(t) ', with P idx ' num2str(i)])
                fprintf('Should be \t Is\n')
                [testSetsWF(t).p(:,i), p] %#ok<NOPRT>
                ok=false;
                fprintf('\tFailed\n')
                continue
            end
            if max(abs(testSetsWF(t).mu(i)-mu))>zeta
                display(['FAIL, wrong Lagrangian multiplier, test No. ' num2str(t) ', with P idx ' num2str(i)])
                ok=false;
            end
            fprintf('\tPassed\n')
        end
    end
catch e
    disp('FAIL, error');
    disp(getReport(e,'extended'))
    ok = false;
end
if ok
    disp('OK')
    fprintf('--- All tests passed ---\n\n')
end
