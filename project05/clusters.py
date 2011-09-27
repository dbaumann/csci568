import random

import data
import distance
import prototype

import pprint
pp = pprint.PrettyPrinter(indent=2)



def kmeans(data, k=4, distance=distance.euclidean, prototype=prototype.rand):
	attributes = range(len(data[0]))

	centroids = prototype(data, k)

	print "initial centroids:"
	print centroids

	clusters_last = None
	for t in range(100):
		print 'Iteration %d' % t
		clusters = [[] for i in range(k)]

		#assign each object to the closest centroid
		for object_num in range(len(data)):
			obj = data[object_num]
			assigned_cluster_num = random.choice(range(k))

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
			attr_averages = [0.0] * len(attributes)

			if len(clusters[i]) > 0:
				for object_num in clusters[i]:
					for attr_num in attributes:
						attr_averages[attr_num] += data[object_num][attr_num]
				
				for attr_num in attributes:
					attr_averages[attr_num] /= len(clusters[i])
				
				centroids[i] = attr_averages
	
	return clusters, centroids

def cluster_sse(data, cluster, centroid, distance=distance.euclidean):
	return sum([pow(distance(data[object_num], centroid), 2) for object_num in cluster])

iris_data, iris_keys = data.iris()


#for euclidean
for i in range(2, 5):
	print "kmeans result clusters based on euclidean distance for k = %d:" % i

	clusters, centroids = kmeans(iris_data, k=i, distance=distance.euclidean,
							prototype=prototype.avg)

	sse_values = []

	for j in range(i):

		sse_values.append(cluster_sse(iris_data, clusters[j], centroids[j],
							distance=distance.euclidean)) 

		print "%d {size: %d, sse: %f, centroid:[%s]}" % \
			(j,
			len(clusters[j]),
			sse_values[j],
			', '.join(['{:.3}'.format(attr_val) for attr_val in centroids[j]]))

	print "total sse: %f" % sum(sse_values)

	print "\n"
