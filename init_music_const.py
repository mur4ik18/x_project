# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:55:04 2024

@author: PIAT F.
"""
# create class midi player
# add renversemet for chords | use modulo and after use sort like this we will get this [4, 7, 12] -> [0, 4, 7] -> M
# realiser profiles for chord
profileM= [6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88]
profilem = [6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17]

# calcule Distance between two profiles, calculate corralation
# TODO tester les constructors de Chord et Chord_keyboard

# better to use tuples instead of lists?
dict_intervals = {'M': [0,4,7], 'm':[0,3,7] ,'M7': [0,3,7,11], 'm7': [0,3,7,10], '7': [0,4,7,10], '7sus4': [0,5,7,10], '4': [0,5,7], '2': [0,2,7], '6': [0,4,7,9], 'm6': [0,3,7,9], '6sus4': [0,5,7,9], 'dim': [0,3,6], 'aug': [0,4,8] , '5': [0,7] }



class Chroma:
    
    #static or instance attribute depending on whether prefix is class name or instance
    chroma=('Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'Sol', 'Sol#', 'La', 'La#', 'Si')
    
    def __init__(self,nom):
        self.nom = nom
        self.index = Chroma.chroma.index(nom)
        
    def __str__(self):
        return self.nom
    
    def transpose(self, n ):
        return Chroma.chroma [ (self.index+n) % len(Chroma.chroma) ]
        

class Note(Chroma):
# define a note by specifying its midi number or name+octave
    """
    def __init__(self, chroma, octave):
        Chroma().__init__(self, chroma.nom)
        self.octave = octave
        self.midiNum = self.index + self.octave*12
    """
    def __init__(self, nom, octave):
        Chroma().__init__(self, nom)
        self.octave = octave
        self.midiNum = self.index + octave*12
        
    def __init__(self, midiNum):
        Chroma().__init__(self, Chroma.chroma[midiNum%12])
        self.octave = midiNum//12
        self.midiNum = midiNum

    # add get Message Midi with note on and note off


# List of the main kinds of chords used in music theory
class Type_accord:
    type_accord = list(dict_intervals);

    def getAccordType(intervals):
        for key, value in dict_intervals.items():
            if value == intervals:
              return key  


class Chord(Chroma):
    # 4 constructors diff.
    # p1 String(nom de chroma), Obj chroma
    # p2 String(TypeAccord), intervals

    def __init__(self , nom, type_accord):
        Chroma().__init__(self, nom)
        self.type_accord = type_accord
        self.intervals = dict_intervals[type_accord]
        
    def __init__(self , nom, intervals):
        Chroma().__init__(self, nom)
        self.intervals = intervals
        #TODO if non need to search reverse of chord
        self.type_accord = Type_accord.getAccordType(intervals)
        
    def __str__(self):
        return super().__str__() + ' ' + self.intervals.__str__()
    
    def transpose(self, n ):
        super().transpose(n)

    def getProfile():
        pass

    def computeDistance(profile2:list = []):
        pass # return correlation entre self.getProfile et profile2

#cord for play
#TODO get midiMessage
class Chord_keyboard(Chord,Note):
    # 
    def __init__(self, chord, octave):
        Chord().__init__(self,chord)
        Note().__init__(self,chord.nom ,octave)


#----------------------------------------------------

dict_chords = {}

c = Chroma('Sol')
print(Chroma.chroma)

for ch in Chroma.chroma:
    for t in Type_accord.type_accord:
        print(t)
        dict_chords[t] = Chord(ch+t, t, dict_intervals[t] );
        print(dict_chords[t] );

       
#print(dict_chords)
