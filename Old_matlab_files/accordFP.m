classdef accordFP
    properties 
        hauteurs
        type_accord = strtrim(evalc('disp(type_accords.Inconnu)'));
        nbnotes
    end
    properties (Constant, Hidden)
        notes_type = {[0 4 7] [0 3 7] [0 3 7 11] [0 3 7 10] [0 4 7 10] [0 5 7 10] [0 3 7 11] [0 5 7] [0 2 7] [0 4 7 9] [0 3 7 9] [0 5 7 9] [0 3 6] [0 4 8]};
    end
    
    
    methods
        function obj = accordFP(EnsNotes)
            if isa(EnsNotes,'double')
                EnsNotes = unique(EnsNotes);
                obj.nbnotes = length(EnsNotes);
                obj.hauteurs = EnsNotes - EnsNotes(1);
%                 k = 1;
%                 while k <= length(a.notes_type) && ~isequal(a.hauteurs, a.notes_type{k})
%                     k = k+1;
%                 end
%                 if k <= length(a.notes_type)
%                     a.type_accord = strtrim(evalc('disp(type_accords(k))'));
%                 end
                    nbTypes = type_accords.getNbTypeAccords();
                    matEnsNotes = ones(nbTypes,1) * obj.hauteurs;  % duplique vecteur de notes 
                    cellmatEnsNotes = mat2cell(matEnsNotes, ones(nbTypes,1), length(obj.hauteurs) );
                    disp(obj.notes_type)
                    disp(cellmatEnsNotes')
                    a.type_accord = type_accords ( find( cellfun(@isequal, cellmatEnsNotes' ,obj.notes_type)) ); 
            else
                obj.type_accord = strtrim(evalc('disp(EnsNotes)'));
                obj.hauteurs = cell2mat(obj.notes_type(EnsNotes));
                obj.nbnotes = length(obj.hauteurs);
            end
        end

        
        function s = GetNomType(a)
            s = evalc( 'disp(a.type_accord)' ); % converts enumerated type to string (using the conversion done by disp)
        end
%{
        function a = ajouter_notes(a,nb)
            if nargin < 2	%defaut ajoute 1 note
                nb = 1;
            end
            base = unique(mod(a.hauteurs,12));
            b = length(base);
			nb = nb + a.nbnotes;     %nb final de notes
			nbOctaves = ceil(nb/b);  % combien d'octave cela couvre
			vectNotes = base' * ones(1,nbOctaves);   % duplique le vecteur de base
			decalageOctaves =  ones(b,1) * (12*(0:nbOctaves-1)); % cree colonnes de 0, 12, 24...
            vect = (vectNotes + decalageOctaves);   
			a.hauteurs = vect (1:nb);    %garder seulement les nb qui nous interessent
a.nbnotes = length(a.hauteurs);
        end
        
        function a = supprimer_notes(a,pos)
            if nargin < 2
                pos = a.nbnotes;
            end
            a.hauteurs(pos) = [];
            a.nbnotes = length(a.hauteurs);
        end
        
         function r = cree_renversement(a,nb)
            r = a; % Création de l'accord 'r' prêt à être renversé
            if nargin < 2
                nb = 1; % Un renversement par défaut
            end
            nb = mod( nb, a.nbnotes); % il ne peut y avoir plus de renversements que de notes
            
            r.hauteurs = circshift ( r.hauteurs, [0 nb]);  %permutation circulaire
            r.hauteurs = mod (r.hauteurs - r.hauteurs(1) , 12);% met le 1er a 0 et le reste entre 0 et 12

         end
%}        
    end
end