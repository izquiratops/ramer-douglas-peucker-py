import numpy as np
from numpy import linalg as la

def perpendicularDistance(point, line):
	return np.divide(
		la.norm(np.cross(np.subtract(line[1], line[0]), np.subtract(line[0], point))),
		la.norm(np.subtract(line[1], line[0])))

def douglify(raw_data, epsilon):
	maxDistanceIndex = -1
	maxDistanceValue = 0
	end = raw_data.shape[0]
	ResultList = np.empty([0], dtype='float32')

	for index, element in enumerate(raw_data):
		if index == 0:
			continue

		else:
			distance = perpendicularDistance(raw_data[index], (raw_data[0], raw_data[-1]))
			if (distance > maxDistanceValue):
				maxDistanceIndex = index
				maxDistanceValue = distance

	if maxDistanceValue > epsilon:
		# A - B - C - D - E - F - G - H - I - J - K - L - M
		# A --- (recursive1) ---- G ---- (recursive2) --- M
		# recursive1: [A : G]
		# recursive2: [G : M]
		recursive1 = douglify(raw_data[:maxDistanceIndex+1], epsilon)
		recursive2 = douglify(raw_data[maxDistanceIndex:], epsilon)
		return np.vstack((recursive1[:-1], recursive2))
	else:
		return np.vstack((raw_data[0], raw_data[-1]))