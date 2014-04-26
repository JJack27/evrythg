function test_worstCaseRate(filename)

if nargin<1, filename = 'testData'; end

load(filename)

zeta = 1e-2;

ok = true;
disp('Testing worstCaseRate')
try
    for t=1:length(testSetsWCR)
        for i=1:length(testSetsWCR(t).N)
            fprintf('Running test %d.%d\n', t, i)
            [R,s,mu] = worstCaseRate(testSetsWCR(t).p,testSetsWCR(t).N(i));
            if max(abs(testSetsWCR(t).R(i)-R))>zeta
                display(['FAIL, wrong rate, test No. ' num2str(t) ', with noise power ' num2str(testSetsWCR(t).N(i))])
                keyboard
                ok=false;
            end
            if max(abs(testSetsWCR(t).s(:,i)-s))>zeta
                display(['FAIL, wrong worst case powers, test No. ' num2str(t) ', with noise power ' num2str(testSetsWCR(t).N(i))])
                fprintf('Should be \t Is\n')
                [testSetsWCR(t).s(:,i), s] %#ok<NOPRT>
                keyboard
                ok=false;
            end
            if max(abs(testSetsWCR(t).mu(i)-mu))>zeta
                fprintf('Should be: %f, is %f\n', ttestSetsWCR(t).mu(i), mu);
                display(['FAIL, wrong Lagrangian multiplier, test No. ' num2str(t) ', with noise power ' num2str(testSetsWCR(t).N(i))])
                keyboard
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
    fprintf('--- All tests passed ---\n\n')
end

