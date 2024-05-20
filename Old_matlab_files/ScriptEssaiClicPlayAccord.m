global  myMidiPlayer ma
myMidiPlayer = Player()
ma = MesureAccord(accord_2018('Fa',2), Arpege(TonalPicks().notesToPick))

map = CreateMap24Profiles();

dcm_obj = datacursormode(figure);
set(dcm_obj,'UpdateFcn',@FonctionDataCursorPlayChord)

surf(map)
colormap(jet)
shading INTERP
