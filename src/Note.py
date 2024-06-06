from Chroma import Chroma

class Note(Chroma):
# define a note by specifying its midi number or name+octave
    """
    def __init__(self, chroma, octave):
        Chroma().__init__(self, chroma.nom)
        self.octave = octave
        self.midiNum = self.index + self.octave*12
    """
    def __init__(self, nom, octave):
        Chroma().__init__(nom)
        self.octave = octave
        self.midiNum = self.index + octave*12
        
    def __init__(self, midiNum):
        super().__init__(Chroma.chroma[midiNum%12])
        self.octave = midiNum//12
        self.midiNum = midiNum

    def getMidiMessage(self, velocity, channel, time):
        return {'note': self.midiNum, 'velocity': velocity, 'type': 'note_on', 'channel': channel, 'time': time}
