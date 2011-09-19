from math import sqrt

"""A set of similarity metrics.
Values closer to 1 represent a better match."""

def euclidean(vector1, vector2):
	"""Traditional linear distance between the endpoints of two vectors of numeric values.
	If one vector is longer than another, the extra values of the longer are ignored."""

	shortest_length = min(len(vector1), len(vector2))

	sum_of_squares = sum([pow(vector1[i] - vector2[i], 2) for i in range(shortest_length)])

	#greater distance shold mean lower similarity
	return 1/(1+sqrt(sum_of_squares))

def smc(vector1, vector2):
	"""Simple measure of similarity for vectors of binary values.
	If one vector is longer than another, the extra values of the longer are ignored.

	Raises ValueError for non-binary input vector."""

	union = list(set(vector1) | set(vector2))
	if(max(union) > 1 or min(union) < 0): raise ValueError

	shortest_length = min(len(vector1), len(vector2))
	match0,match1 = 0,0

	for i in range(shortest_length):
		if(vector1[i]==0 and vector2[i]==0): match0 += 1
		if(vector1[i]==1 and vector2[i]==1): match1 += 1
		
	return float(match0 + match1)/shortest_length

def jaccard(vector1, vector2):
	union = list(set(vector1) | set(vector2))
	if(max(union) > 1 or min(union) < 0): raise ValueError

	shortest_length = min(len(vector1), len(vector2))
	match0,match1 = 0,0

	for i in range(shortest_length):
		if(vector1[i]==0 and vector2[i]==0): match0 += 1
		if(vector1[i]==1 and vector2[i]==1): match1 += 1
		
	return float(match1)/(shortest_length-match0)
