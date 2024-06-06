from Chord import Chord
from Note import Note
from Chroma import Chroma
from Support import *
from Chord_keyboard import Chord_keyboard

#----------------------------------------------------
if __name__ == "__main__":
    dict_chords = {}

    for chroma in Chroma.chroma:
        for type in Type_accord.type_accord:
            dict_chords[type] = Chord(chroma, type)

    print(dict_chords)
    x = Chord_keyboard(dict_chords['M'], 60)
    print(x.getMidiMessage(0.2, 100, 0))

    
    
