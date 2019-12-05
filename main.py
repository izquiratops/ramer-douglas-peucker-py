import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

x = np.arange(0.0, 5.0, 0.05)
y = f(x)

# Creates two subplots and unpacks the output array immediately
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
fig = matplotlib.pyplot.gcf()
size = 8
fig.set_size_inches(2*size, 1*size, forward=True)
fig.canvas.set_window_title('Series Reducer')

# fig.suptitle('Series Reducer')
ax1.set_title('Raw Points')
ax1.plot(x, y, 'bo', x, y, 'k')
ax2.set_title('Ramer–Douglas–Peucker')
ax2.plot(x, y, 'bo', x, y, 'k')

plt.show()