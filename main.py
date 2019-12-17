import sys
import douglas
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# python main.py 0.55
try:
	epsilon = float(sys.argv[1])
except Exception as ex:
	print(ex)
	exit(0)

def setup_figure(raw_data, douglas_data):
	# Creates two subplots and unpacks the output array immediately
	fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)
	fig = matplotlib.pyplot.gcf()
	size = 8
	fig.set_size_inches(2*size, 1*size, forward=True)
	fig.canvas.set_window_title('Series Reducer')

	# fig.suptitle('Series Reducer')
	ax1.set_title('Raw Points')
	ax1.plot(raw_data[0], raw_data[1], 'bo', raw_data[0], raw_data[1], 'k')
	ax2.set_title('Ramer–Douglas–Peucker, Epsilon: ' + str(epsilon))
	ax2.plot(douglas_data[0], douglas_data[1], 'bo', douglas_data[0], douglas_data[1], 'k')

def f(t):
	return np.exp(-0.5*t) * np.cos(np.pi*t)

def generate_data():
	raw_x = np.arange(0.0, 5.0, 0.05, dtype='float32')
	raw_y = f(raw_x)
	return np.column_stack((raw_x, raw_y))

raw_data = generate_data()
douglas_data = douglas.douglify(raw_data, epsilon)
setup_figure(np.transpose(raw_data), np.transpose(douglas_data))
plt.show()