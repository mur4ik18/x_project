from Chord import Chord
from Note import Note
from Chroma import Chroma
from Support import *
from Chord_keyboard import Chord_keyboard
from OurMidi import OurMidi


import numpy as np



def normolize(arr):
    # chaque element de arr diviser par v
    v = np.linalg.norm(arr)
    print(v)
    res = []
    for i in arr:
        res.append(i/v)
    return res

def corr(arr, arr2):
    if len(arr) != len(arr2):
        raise ValueError("Length of arrays isn't same", arr, arr2)
    a = np.array(arr)
    b = np.array(arr2)

    #a = a - np.mean(a)
    #b = b - np.mean(b)
    print(a,b)
    print(a*b)
    print(np.linalg.vector_norm(arr), np.linalg.vector_norm(arr2))
    return sum(a*b)/(np.linalg.vector_norm(arr)*np.linalg.vector_norm(arr2))


    
#----------------------------------------------------
if __name__ == "__main__":
    dict_chords = {}
    a = [4,4,4]
    
    print(corr([6.2,2.33,2.8],[2.8,6.2,2.33]))
    
    # m = OurMidi("Entr√©e virtuelle GarageBand")
    
    # for chroma in Chroma.chroma:
    #     for type in Type_accord.type_accord:
    #         dict_chords[type] = Chord(chroma, type)

    # print(dict_chords)
    # data = []
    # data.extend(Chord_keyboard(dict_chords['M'], 60+12).getMidiMessage(0.1, 100, 0))
    # data.extend(Chord_keyboard(dict_chords['m'], 60+11).getMidiMessage(0.1, 100, 0))
    # #data.extend(Chord_keyboard(dict_chords['7'], 60).getMidiMessage(0.1, 100, 0))
    # m.playList(data)

    
    
