CMajProfile = [0.65 -0.3 0.0 -0.25 0.2 0.15 -0.25 0.4 -0.25 0.05 -0.25 -0.15];
CminProfile = [0.65 -0.25 -0.05 0.4 -0.3 -0.05 -0.3 0.3 0.1 -0.25 -0.1 -0.15];

global profileMajRound profileMinRound;
profileMajRound = [CMajProfile CMajProfile];  % to access easily a circular permutation. start from right to fet the order C, C#, D...
profileMinRound = [CminProfile CminProfile];

%plot(CminProfile)