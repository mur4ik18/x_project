import mido
import time
import rtmidi


midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
print(available_ports)
midiout.open_port(3)

note_on = [0x90, 60, 112] # channel 1, middle C, velocity 112
midiout.send_message([0x90, 60, 100])
midiout.send_message([0x90, 64, 100])
midiout.send_message([0x90, 67, 100])

