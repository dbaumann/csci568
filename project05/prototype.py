import random

def rand(data, k):
	attributes = range(len(data[0]))

	#determine the range of values for each attribute
	attribute_ranges = [(min([obj[i] for obj in data]), max([obj[i] for obj in data]))
				for i in attributes]

	#select k points as initial centroids
	return [[attribute_ranges[i][0] +
					(random.random()*(attribute_ranges[i][1]-attribute_ranges[i][0]))
					for i in attributes]
				for j in range(k)]

def avg(data, k):
	attributes = range(len(data[0]))

	attr_averages = [0.0] * len(attributes)

	#select k points as initial centroids
	for object_num in range(len(data)):
		for attr_num in attributes:
			attr_averages[attr_num] += data[object_num][attr_num]
		
	for attr_num in attributes:
		attr_averages[attr_num] /= len(data)
		
	return [attr_averages for i in range(k)]