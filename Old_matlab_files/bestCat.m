function [maxactiv, winner] = bestCat(inputF,W1)
%returns the most resonating prototype and resonance value
%   we can do the same with match values instead, change argument of max

nbcats = size(W1,1);
match = zeros(1, nbcats);
H = zeros(1, nbcats);

for i=1:nbcats
  activ =  norm( min(inputF',W1(:,i)) ,1);
  match(i) = activ;
  H(i) =  activ /  ( a+norm(W1(:,i),1) ); %eviter division par 0: a=1
end


%nbnomatch=0;

[maxactiv, winner ] = max(H);


% recherche d'un bon match dans l'ordre donné par resonances H

%  while ( (match(winner) < vigil) & any(H(1:nbcat)+1) ),
%   H(winner)= -1;                        %disable not good enough winner
%   [dum winner] = max(H);                %and get next candidate
%   nbnomatch=nbnomatch+1;
%  end 

end

