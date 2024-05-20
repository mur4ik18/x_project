global  myMidiPlayer ma
myMidiPlayer = Player()
 ma = MesureAccord(accord_2018('Fa',2), Arpege(TonalPicks().notesToPick))
 
 dcm_obj = datacursormode(figure);
 set(dcm_obj,'UpdateFcn',@EssaiFonctionDataCursor)
 
 ma.play(myMidiPlayer); 
 plot([1 3 2])