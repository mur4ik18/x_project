classdef accord
    properties
        hauteurs % Vecteur d'intervalles (Ex: [0 4 7] pour l'accord majeur)
        type_accord = 'Inconnu'; % Valeur par d�faut
        nbnotes % Taille du tableau hauteurs
    end
    properties (Constant, Hidden)
        type_accords = {'M' 'm' 'M7' 'm7' '7' '7sus4' 'mM7' '4' '2' '6' 'm6' '6sus4' 'dim' 'aug' '5'};
        % Liste des diff�rents genres d'accords utilis�s en th�orie de la musique
        notes_type = {[0 4 7] [0 3 7] [0 3 7 11] [0 3 7 10] [0 4 7 10] [0 5 7 10] [0 3 7 11] [0 5 7] [0 2 7] [0 4 7 9] [0 3 7 9] [0 5 7 9] [0 3 6] [0 4 8] [0 7]};
    end % Liste des diff�rentes hauteurs correspondant au tableau type_accords ci-dessus
    
    
    methods
        function a = accord(EnsNotes)
            if isa(EnsNotes,'double')
                % Si "EnsNotes" est un tableau d'entiers
                EnsNotes = unique(EnsNotes); % Tri du tableau et
                                             % suppression des doublons.
                a.nbnotes = length(EnsNotes); % Calcul du nombre de notes
                a.hauteurs = EnsNotes - EnsNotes(1);
                % Calcul de 'hauteurs' en mettant la premi�re valeur � 0.
                k = 1;
                while k <= length(a.notes_type) && ~isequal(a.hauteurs, a.notes_type{k})
                    k = k+1; % Recherche de l'indice de 'hauteurs' dans le
                             % tableau 'notes_type' d�fini en propri�t� 
                             % statique de 'a'
                end
                if k <= length(a.notes_type)
                    a.type_accord = a.type_accords{k};
                end % Recherche du type d'accord de 'a'
            elseif ismember(EnsNotes,a.type_accords) 
                % Si "EnsNotes" n'est pas un tableau d'entiers (dans le cas
                % o� c'est une cha�ne de caract�re)
                a.type_accord = EnsNotes;
                % Copie de "EnsNotes" dans 'type_accord'
                k = 1;
                while k <= length(a.type_accords) && ~isequal(EnsNotes, a.type_accords{k})
                    k = k+1; % Recherche de la valeur de 'hauteurs' dans le
                end          % tableau 'notes_type' � l'aide du tableau
                             % 'type_accords' en propri�t� statique
                if k <= length(a.type_accords)
                    a.hauteurs = a.notes_type{k};
                end
                a.nbnotes = length(a.hauteurs); % Calcul du nombre de notes
            end
        end
        
        function affiche_accord(a)
            disp(a.type_accord);
        end
        
        function a = ajouter_notes(a,nb)
            if nargin < 2
                nb = a.nbnotes; % Par d�faut (ajout d'une octave compl�te)
            end
            base = length(unique(mod(a.hauteurs,12))); % Calcul de la taille
            % du vecteur contenant la premi�re octave des hauteurs de l'accord
            for k = 1:nb
                a.hauteurs = [a.hauteurs 12+a.hauteurs(a.nbnotes+1-base)];
                % Ajout de l'octave de la premi�re hauteur non-octavi�e
                % dans 'hauteurs'
                a.nbnotes = a.nbnotes + 1;
            end % Incr�mentation du nombre de notes
        end
        
        function a = supprimer_notes(a,pos)
            if nargin < 2
                pos = a.nbnotes;
            end
            a.hauteurs(pos) = []; % Suppression des notes aux positions
                                  % d�finies en entr�e (vecteur "pos")
            a.nbnotes = length(a.hauteurs);
        end % Mise � jour du nombre de notes
        
        function r = cree_renversement(a,nb)
            r = a; % Cr�ation de l'accord 'r' pr�t � �tre renvers�
            if nargin < 2
                nb = 1; % Un renversement par d�faut
            end
            j = 1;
            while j <= nb
                r.hauteurs = [a.hauteurs(a.nbnotes-j+1),r.hauteurs(1:a.nbnotes-1)];
                % La derni�re valeur de 'hauteurs' devient la premi�re
                j = j+1;
            end
            r.hauteurs = mod(r.hauteurs-r.hauteurs(1),12);
        end % Ajustement des valeurs de 'hauteurs' en mettant la premi�re
    end     % � 0.
end