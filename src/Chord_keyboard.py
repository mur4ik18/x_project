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
        return self.note.getMidiMessage(velocity, channel, time)
