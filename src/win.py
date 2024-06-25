import pygame
import pygame.midi
from time import sleep
import mido
from OurMidi import OurMidi

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

#m = OurMidi()
x = [
    {'note': 60, 'velocity': 100, 'type': 'note_on', 'channel': 0, 'time': 0},
    {'note': 64, 'velocity': 100, 'type': 'note_on', 'channel': 0, 'time': 0.2},
    {'note': 67, 'velocity': 100, 'type': 'note_on', 'channel': 0, 'time': 0.2},
    {'note': 67, 'velocity': 100, 'type': 'note_on', 'channel': 0, 'time': 0},
    {'note': 64, 'velocity': 100, 'type': 'note_on', 'channel': 0, 'time': 0.2},
    {'note': 60, 'velocity': 100, 'type': 'note_on', 'channel': 0, 'time': 0.2}]
#m.playList(x)
#print(m.mid)
#m.mid.save("output.mid")


# Initialize Pygame MIDI
pygame.midi.init()
for i in range(pygame.midi.get_count()):
    print(i, pygame.midi.get_device_info(i))

# Open an output port
player = pygame.midi.Output(pygame.midi.get_default_output_id())


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player.note_on(60, 60)
        player.note_off(60)
       # pygame.mixer.music.play()
    screen.fill("purple")
    pygame.display.flip()
    clock.tick(60)

    
del player
pygame.quit()
