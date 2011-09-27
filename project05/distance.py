from math import sqrt

def euclidean(vector1, vector2):
	sum_of_squares = sum([pow(vector1[i] - vector2[i], 2) for i in range(len(vector1))])

	return sqrt(sum_of_squares)


