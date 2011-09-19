from math import sqrt

"""A set of similarity metrics.
Values closer to 1 represent a better match."""

def euclidean(vector1, vector2):
	"""Traditional linear distance between the endpoints of two vectors."""

	sum_of_squares = sum([pow(vector1[i] - vector2[i], 2) for i in range(len(vector1))])

	#greater distance shold mean lower similarity
	return 1/(1+sqrt(sum_of_squares))
