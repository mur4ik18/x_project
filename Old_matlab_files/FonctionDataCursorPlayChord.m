function output_txt = FonctionDataCursorPlayChord(obj,event_obj)
% Display the position of the data cursor
% obj          Currently not used (empty)
% event_obj    Handle to event object
% output_txt   Data cursor text string (string or cell array of strings).

pos = get(event_obj,'Position');
y = pos(2)  % prototype selected
 

tonic = Chroma (mod(y-1,12) +1)
mode = 1+ floor((y-1)/12)
chord = accord_2018(tonic,mode)
global  myMidiPlayer
%ma = MesureAccord(accord_2018('Fa',2), Arpege(TonalPicks().notesToPick))
ma = MesureAccord(chord)
ma.play(myMidiPlayer); 


output_txt = {chord.char(),['X: ',num2str(pos(1),4)],['Y: ',num2str(pos(2),4)]};
% If there is a Z-coordinate in the position, display it as well
if length(pos) > 2
    output_txt{end+1} = ['Z: ',num2str(pos(3),4)];
end

