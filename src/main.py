from Chord import Chord
from Note import Note
from Chroma import Chroma
from Support import *
from Chord_keyboard import Chord_keyboard
from OurMidi import OurMidi

#----------------------------------------------------
if __name__ == "__main__":
    dict_chords = {}
    m = OurMidi("Entr√©e virtuelle GarageBand")
    
    for chroma in Chroma.chroma:
        for type in Type_accord.type_accord:
            dict_chords[type] = Chord(chroma, type)

    print(dict_chords)
    data = []
    data.extend(Chord_keyboard(dict_chords['M'], 60+12).getMidiMessage(0.1, 100, 0))
    data.extend(Chord_keyboard(dict_chords['m'], 60+11).getMidiMessage(0.1, 100, 0))
    #data.extend(Chord_keyboard(dict_chords['7'], 60).getMidiMessage(0.1, 100, 0))
    m.playList(data)

    
    
