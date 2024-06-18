from Chord import Chord
from Note import Note
from Chroma import Chroma

#cord for play
#TODO get midiMessage
class Chord_keyboard(Chord,Note):

    def __init__(self, chord, note):
        self.chord = chord
        self.note = Note(note)

    def getMidiMessage(self, time, velocity, channel):
        ret = []
        for i in self.chord.intervals:
            ret.append(Note(self.note.midiNum+i).getMidiMessage(velocity, channel, time))
        return ret
