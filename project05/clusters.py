import random

import data
import distance
import prototype

class clustering:

	def __init__(self, data, clusters, centroids, distance=distance.euclidean):
		self.data = data
		self.clusters = clusters
		self.centroids = centroids
		self.distance = distance

	def describe(self):
		sse_values = []

		for j in range(i):

			sse_values.append(self.cluster_sse(j)) 

			print "%d {size: %d, sse: %f, centroid:[%s]}" % \
				(j,
				len(self.clusters[j]),
				sse_values[j],
				', '.join(['{:.5}'.format(attr_val) for attr_val in self.centroids[j]]))

		total_sse = sum(sse_values)

		print "total sse: %f" % total_sse
		print "\n"

	def cluster_sse(self, index):
		return sum([pow(self.distance(self.data[object_num], self.centroids[index]), 2)
						for object_num in self.clusters[index]])
	
	def total_sse(self):
		return sum([self.cluster_sse(i) for i in range(len(self.clusters))])




def kmeans(data, k=4, distance=distance.euclidean, prototype=prototype.rand):
	attributes = range(len(data[0]))

	centroids = prototype(data, k)

	clusters_last = None
	for t in range(1, 101):
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
	
	print "kmeans finished after %d iterations" % t
	
	return clusters, centroids

def cluster_sse(data, cluster, centroid, distance=distance.euclidean):
	return sum([pow(distance(data[object_num], centroid), 2) for object_num in cluster])

def total_sse(data, clusters, centroids, distance=distance.euclidean):
	return sum([cluster_sse(data, clusters[i], centroids[i], distance)
					for i in range(len(clusters))])

def summary_stats(data, keys):
	attributes = range(len(data[0]))

	attr_ranges = [(min([obj[i] for obj in data]), max([obj[i] for obj in data]))
				for i in attributes]

	attr_averages = [sum([obj[i] for obj in data])/len(data) for i in attributes]


	attr_strings = []

	for i in attributes:
		attr_strings.append("%.3f-->%.3f (%.3f)" % \
							(attr_ranges[i][0],attr_ranges[i][1], attr_averages[i]))

	return "[%s]" % ', '.join(attr_strings)


def print_clustering(data, clusters, centroids, distance=distance.euclidean):
	sse_values = []

	for j in range(i):

		sse_values.append(cluster_sse(iris_data, clusters[j], centroids[j], distance)) 

		print "%d {size: %d, sse: %f, centroid:[%s]}" % \
			(j,
			len(clusters[j]),
			sse_values[j],
			', '.join(['{:.5}'.format(attr_val) for attr_val in centroids[j]]))

	total_sse = sum(sse_values)

	print "total sse: %f" % total_sse
	print "\n"


iris_data, iris_keys = data.iris()

stats = summary_stats(iris_data, iris_keys)

#for euclidean
optimal_clustering = 0
minimal_sse = 9999
all_clusterings = []

for t in range(20):

	i = 3

	print "iris statistics:"
	print stats

	print "kmeans result clusters based on euclidean distance for k = %d (trial %d):" % (i, t)

	clusters, centroids = kmeans(iris_data, k=i, distance=distance.euclidean,
							prototype=prototype.avg)

	new_clustering = clustering(iris_data, clusters, centroids)

	new_clustering.describe()

	current_sse = new_clustering.total_sse()

	if(current_sse < minimal_sse):
		optimal_clustering = t
		minimal_sse = current_sse

	all_clusterings.append(new_clustering)


print "optimal clustering:"
all_clusterings[optimal_clustering].describe()