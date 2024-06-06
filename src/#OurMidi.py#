import mido
import rtmidi

class OurMidi:
    def __init__(self, output_name):
        mido.set_backend('mido.backends.rtmidi')   
        mido.open_output(output_name)
        self.mid = mido.MidiFile()
    
    def playList(self, music):
        if type(music[0]) == dict:
            print('Converting dict to list')
            music = self.dictToList(music) 
        track = mido.MidiTrack()
        self.mid.tracks.append(track)
    
        for i in music:
            track.append(i)

        with mido.open_output() as outport:
            for msg in self.mid.play():
                outport.send(msg)

    def dictToList(self, music:dict):
        current_tempo = 500000  # Default 500,000 microseconds per beat (120 BPM)
        ticks_per_beat = self.mid.ticks_per_beat
        def seconds_to_ticks(seconds, tempo, ticks_per_beat):
            microseconds_per_beat = tempo
            seconds_per_beat = microseconds_per_beat / 1000000.0
            ticks_per_second = ticks_per_beat / seconds_per_beat
            return int(seconds * ticks_per_second)
        musicList = []
        for event in music:
            if event['type'] == 'note_on':
                ticks = seconds_to_ticks(event['time'], current_tempo, ticks_per_beat)
                musicList.append(mido.Message(event['type'], note=event['note'], velocity=event['velocity'], channel=event['channel'], time=ticks))
        return musicList
    
if __name__ == '__main__':
    m = OurMidi("Entr√©e virtuelle GarageBand")
    x = [
    {'note': 60, 'velocity': 100, 'type': 'note_on', 'channel': 0, 'time': 0},
    {'note': 64, 'velocity': 100, 'type': 'note_on', 'channel': 0, 'time': 0.2},
    {'note': 67, 'velocity': 100, 'type': 'note_on', 'channel': 0, 'time': 0.2},
    {'note': 67, 'velocity': 100, 'type': 'note_on', 'channel': 0, 'time': 0},
    {'note': 64, 'velocity': 100, 'type': 'note_on', 'channel': 0, 'time': 0.2},
    {'note': 60, 'velocity': 100, 'type': 'note_on', 'channel': 0, 'time': 0.2}]
    m.playList(x)