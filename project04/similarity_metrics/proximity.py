from math import sqrt

"""A set of similarity metrics.
Values closer to 1 represent a better match."""

def euclidean(vector1, vector2):
	"""Traditional linear distance between the endpoints of two vectors of numeric values.
	
	Raises ValueError if one vector is longer than another."""

	if(len(vector1) != len(vector2)): raise ValueError

	sum_of_squares = sum([pow(vector1[i] - vector2[i], 2) for i in range(len(vector1))])

	#greater distance shold mean lower similarity
	return 1/(1+sqrt(sum_of_squares))

def smc(vector1, vector2):
	"""Simple measure of similarity for vectors of binary values.

	Raises ValueError for non-binary input vector.
	Raises ValueError if one vector is longer than another."""

	union = list(set(vector1) | set(vector2))
	if(max(union) > 1 or min(union) < 0): raise ValueError

	if(len(vector1) != len(vector2)): raise ValueError

	match0,match1 = 0,0

	for i in range(len(vector1)):
		if(vector1[i]==0 and vector2[i]==0): match0 += 1
		if(vector1[i]==1 and vector2[i]==1): match1 += 1
		
	return float(match0 + match1)/len(vector1)

def jaccard(vector1, vector2):
	"""Measure of similarity for vectors of binary values. Non-presence matches are
	disregarded.

	Raises ValueError for non-binary input vector.
	Raises ValueError if one vector is longer than another."""
	union = list(set(vector1) | set(vector2))
	if(max(union) > 1 or min(union) < 0): raise ValueError

	if(len(vector1) != len(vector2)): raise ValueError

	match0,match1 = 0,0

	for i in range(len(vector1)):
		if(vector1[i]==0 and vector2[i]==0): match0 += 1
		if(vector1[i]==1 and vector2[i]==1): match1 += 1
		
	return float(match1)/(len(vector1)-match0)

def pearson(vector1, vector2):
	"""Measure of similarity for vectors of numeric values.

	Return values in [-1,0) indicate dissimilarity.

	Raises ValueError if one vector is longer than another."""

	if(len(vector1) != len(vector2)): raise ValueError

	numerator = __covariance(vector1, vector2)
	denominator = sqrt(__covariance(vector1, vector1))*sqrt(__covariance(vector2, vector2))

	return numerator/denominator

def __covariance(vector1, vector2):

	if(len(vector1) != len(vector2)): raise ValueError

	vector1_avg = float(sum(vector1))/len(vector1)
	vector2_avg = float(sum(vector2))/len(vector2)

	cov_sum =  sum([(vector1[i]-vector1_avg)*(vector2[i]-vector2_avg)
				for i in range(len(vector1))])

	return cov_sum/(len(vector1) - 1)