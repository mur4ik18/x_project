import matplotlib
from Support import generateProfiles
import pygame
from pygame.locals import *
import matplotlib.backends.backend_agg as agg
import pylab


matplotlib.use("Agg")
M,m = generateProfiles()

fig = pylab.figure(figsize=[4, 4], # Inches
                   dpi=100,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                   )
ax = fig.gca()

M, m = generateProfiles()
for i,t in enumerate(M):
    xs = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    ys = t
    print()
    ax.plot(xs, ys, zs=len(M)-i, zdir='x', alpha=1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
def onclick(event):
    print(event.xdata, event.ydata)

cid = fig.canvas.mpl_connect('button_press_event', onclick)

print(matplotlib.get_backend())

# On the y-axis let's only label the discrete values that we have data for.
ax.set_yticks(range(1,14),['C','Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'Sol', 'Sol#', 'La', 'La#', 'Si'])

canvas = agg.FigureCanvasAgg(fig)
canvas.draw()
renderer = canvas.get_renderer()
raw_data = renderer.tostring_rgb()



pygame.init()

window = pygame.display.set_mode((600, 400), DOUBLEBUF)
screen = pygame.display.get_surface()

size = canvas.get_width_height()

surf = pygame.image.fromstring(raw_data, size, "RGB")
screen.blit(surf, (0,0))
pygame.display.flip()

crashed = False
while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
