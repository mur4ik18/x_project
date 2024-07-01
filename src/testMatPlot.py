import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from Support import *

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(projection='3d')

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

plt.show()
