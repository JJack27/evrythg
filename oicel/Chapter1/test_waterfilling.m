function test_waterfilling(filename)

if nargin<1, filename = 'testData'; end

load(filename)

zeta = 1e-2;

ok = true;
disp('Testing waterfilling')
try
    for t=1:length(testSetsWF)
        for i=1:length(testSetsWF(t).P)
            [R,p,mu] = waterfilling(testSetsWF(t).h,testSetsWF(t).s,testSetsWF(t).P(i));
            if max(abs(testSetsWF(t).R(i)-R))>zeta
                display(['FAIL, wrong rate, test No. ' num2str(t) ', with N idx ' num2str(i)])
                keyboard
                ok=false;
            end
            if max(abs(testSetsWF(t).p(:,i)-p))>zeta
                display(['FAIL, wrong powers, test No. ' num2str(t) ', with N idx ' num2str(i)])
                keyboard
                ok=false;
            end
            if max(abs(testSetsWF(t).mu(i)-mu))>zeta
                display(['FAIL, wrong Lagrangian multiplier, test No. ' num2str(t) ', with N idx ' num2str(i)])
                keyboard
                ok=false;
            end
        end
    end
catch e
    disp('FAIL, error');
    disp(getReport(e,'extended'))
    ok = false;
end
if ok
    disp('OK')
end