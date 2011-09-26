import csv
import random
from math import sqrt

import pprint
pp = pprint.PrettyPrinter(indent=2)

def prepare_iris_data():
	reader = csv.reader(open('iris.csv', 'rb'))

	return ([[float(value) for value in row[0:4]] for row in reader],
			['sepal_length','sepal_width','petal_length','petal_width'])

def euclidean(vector1, vector2):
	sum_of_squares = sum([pow(vector1[i] - vector2[i], 2) for i in range(len(vector1))])

	return sqrt(sum_of_squares)

def kmeans_clusters(data, distance=euclidean, k=4):
	attributes = range(len(data[0]))

	#determine the range of values for each attribute
	ranges = [(min([row[i] for row in data]), max([row[i] for row in data]))
				for i in attributes]

	print "ranges are:"
	print ranges

	#select k points as initial centroids
	centroids = [[ranges[i][0] + (random.random()*(ranges[i][1]-ranges[i][0])) for i in attributes]
					for j in range(k)]
	
	print "centroids are:"
	print centroids

	closest_centroids_last = None
	for t in range(100):
		print 'Iteration %d' % t
		closest_centroids = [[] for i in range(k)]

		#assign each point to the closest centroid
		for row_num in range(len(data)):
			row = data[row_num]
			closest_centroid_num = 0

			for cluster_num in range(k):
				d = distance(centroids[cluster_num], row)
				if d < distance(centroids[closest_centroid_num], row):
					closest_centroid_num = cluster_num

			closest_centroids[closest_centroid_num].append(row_num)
		
		#terminate the loop if the centroids list hasn't changed
		if closest_centroids == closest_centroids_last: break
		closest_centroids_last = closest_centroids

		#recompute the centroid of each cluster
		for i in range(k):
			attr_averages = attr_sum = [0.0]*len(attributes)

			if len(closest_centroids[i]) > 0:
				for row_num in closest_centroids[i]:
					for attr_num in attributes:
						attr_sum[attr_num] += data[row_num][attr_num]
				
				for attr_num in attributes:
					attr_averages[attr_num] = attr_sum[attr_num]/len(closest_centroids[i])
				
				centroids[i] = attr_averages
	
	return closest_centroids, centroids

def cluster_sse(data, cluster, centroid, distance=euclidean):
	return sum([pow(distance(data[row_num], centroid), 2) for row_num in cluster])

data, keys = prepare_iris_data()

clusters, centroids = kmeans_clusters(data, k=3)

print "clusters:"
for i in range(len(clusters)):
	print "%d { size: %d, sse: %f}" % (i, len(clusters[i]),cluster_sse(data,clusters[i],centroids[i]))


