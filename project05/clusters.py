import random

import data_sources
import distance

import pprint
pp = pprint.PrettyPrinter(indent=2)



def kmeans(data, distance=distance.euclidean, k=4):
	attributes = range(len(data[0]))

	#determine the range of values for each attribute
	attribute_ranges = [(min([obj[i] for obj in data]), max([obj[i] for obj in data]))
				for i in attributes]

	print "attribute_ranges:"
	print attribute_ranges

	#select k points as initial centroids
	centroids = [[attribute_ranges[i][0] +
					(random.random()*(attribute_ranges[i][1]-attribute_ranges[i][0]))
					for i in attributes]
				for j in range(k)]
	
	print "initial random centroids:"
	print centroids

	clusters_last = None
	for t in range(100):
		print 'Iteration %d' % t
		clusters = [[] for i in range(k)]

		#assign each object to the closest centroid
		for object_num in range(len(data)):
			obj = data[object_num]
			assigned_cluster_num = 0

			for cluster_num in range(k):
				d = distance(centroids[cluster_num], obj)
				if d < distance(centroids[assigned_cluster_num], obj):
					assigned_cluster_num = cluster_num

			clusters[assigned_cluster_num].append(object_num)
		
		#terminate the loop if the centroids list hasn't changed
		if clusters == clusters_last: break
		clusters_last = clusters

		#recompute the centroid of each cluster
		for i in range(k):
			attr_averages = attr_sum = [0.0]*len(attributes)

			if len(clusters[i]) > 0:
				for object_num in clusters[i]:
					for attr_num in attributes:
						attr_sum[attr_num] += data[object_num][attr_num]
				
				for attr_num in attributes:
					attr_averages[attr_num] = attr_sum[attr_num]/len(clusters[i])
				
				centroids[i] = attr_averages
	
	return clusters, centroids

def cluster_sse(data, cluster, centroid, distance=distance.euclidean):
	return sum([pow(distance(data[object_num], centroid), 2) for object_num in cluster])

iris_data, iris_keys = data_sources.iris()

clusters, centroids = kmeans(iris_data, k=3)

print "result clusters:"
for i in range(len(clusters)):
	print "%d {size: %d, sse: %f}" % \
		(i, len(clusters[i]), cluster_sse(iris_data, clusters[i], centroids[i]))


