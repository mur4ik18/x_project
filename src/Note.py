from Chroma import Chroma

class Note(Chroma):
    # do using of Chroma
    def __init__(self, name:str = None, octave:int = None, midiNum:int = None, chroma:Chroma=None):
        if name != None:
            super().__init__(nom = name)
        if midiNum is None and octave is None:
            raise ValueError("midiNum or octave is obligatory")
        
        if midiNum != None:
            super().__init__(Chroma.chroma[midiNum%12])
            self.midiNum = midiNum
            self.octave = midiNum//12
        else:
            self.octave = octave
            self.midiNum = self.index + octave*12
        
        

    
    def getMidiMessage(self, velocity, channel, time):
        return {'note': self.midiNum, 'velocity': velocity, 'type': 'note_on', 'channel': channel, 'time': time}


if __name__ == "__main__":
    # check first constructor
    x = Note(name="Do", octave=4)
    print(x.midiNum, x.nom, x.index, x.octave)
    # check second constructor
    c = Note(midiNum=64)
    print(c.midiNum, c.nom, c.index, c.octave)

    try:
        z = Note(name="Do")
        print(z.midiNum, z.nom, z.index, z.octave)
    except ValueError as e:
        print(e)
