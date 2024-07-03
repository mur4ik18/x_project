import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.proj3d import proj_transform
from Support import *

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(projection='3d')
lines = []
M, m = generateProfiles()
for i,t in enumerate(M):
    xs = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    ys = t
    print()
    line, = ax.plot(xs, ys, zs=len(M)-i, zdir='x', alpha=1)
    lines.append(line)


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
"""
def onclick(event):
    for line in lines:
        # it works
        if line.contains(event)[0]:  # Check if the event occurred near the line
            print(f'Clicked on line index: {line._verts3d[0][0]}')
            print(line.__dict__)
            break
"""

def onclick(event):
    if event.inaxes == ax:
        x2d, y2d = event.x, event.y
        for line in lines:
            xdata, ydata, zdata = line.get_data_3d()

            # Project the 3D data to 2D screen coordinates
            screen_proj = np.array([ax.transData.transform(proj_transform(x, y, z, ax.get_proj())[:2])
                                    for x, y, z in zip(xdata, ydata, zdata)])
            
            dist = np.sqrt((screen_proj[:, 0] - x2d) ** 2 + (screen_proj[:, 1] - y2d) ** 2)
            min_dist_index = np.argmin(dist)
            
            # Get the closest point coordinates in the data space
            x_click, y_click, z_click = xdata[min_dist_index], ydata[min_dist_index], zdata[min_dist_index]
            if dist[min_dist_index] < 5:  # Tolerance for clicking near the line
                print(f'Clicked on line at 3D coordinates (X, Y, Z): ({x_click}, {y_click}, {z_click})')
                print(f'X coordinate on the line where clicked: {x_click}')
                break

cid = fig.canvas.mpl_connect('button_press_event', onclick)

print(matplotlib.get_backend())

# On the y-axis let's only label the discrete values that we have data for.
ax.set_yticks(range(1,14))
#ax.set_yticklabels(['C','Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'Sol', 'Sol#', 'La', 'La#', 'Si'])
plt.show()
