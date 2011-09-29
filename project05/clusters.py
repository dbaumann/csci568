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

	def source_data_summary(self):
		"""
		Produces a summary in the form min-->max (avg) for each attribute of the source data
		"""
		attributes = range(len(self.data[0]))

		attr_ranges = [(min([obj[i] for obj in self.data]), max([obj[i] for obj in self.data]))
					for i in attributes]

		attr_averages = [sum([obj[i] for obj in self.data])/len(self.data) for i in attributes]


		attr_strings = []

		for i in attributes:
			attr_strings.append("%.3f-->%.3f (%.3f)" % \
								(attr_ranges[i][0],attr_ranges[i][1], attr_averages[i]))

		return "[%s]" % ', '.join(attr_strings)

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

	@staticmethod
	def kmeans(data, k=4, distance=distance.euclidean, prototype=prototype.rand):
		"""
		A static factory method providing a kmeans clustering of the source data.
		"""

		result_clustering = clustering(data, clusters=[], centroids=prototype(data, k))

		attributes = range(len(data[0]))

		clusters_last = None
		for t in range(1, 101):
			result_clustering.clusters = [[] for i in range(k)]

			#assign each object to the closest centroid
			for object_num in range(len(data)):
				obj = data[object_num]
				assigned_cluster_num = random.choice(range(k))

				for cluster_num in range(k):
					d = distance(result_clustering.centroids[cluster_num], obj)
					if d < distance(result_clustering.centroids[assigned_cluster_num], obj):
						assigned_cluster_num = cluster_num

				result_clustering.clusters[assigned_cluster_num].append(object_num)
			
			#terminate the loop if the centroids list hasn't changed
			if result_clustering.clusters == clusters_last: break
			clusters_last = result_clustering.clusters

			#recompute the centroid of each cluster
			for i in range(k):
				attr_averages = [0.0] * len(attributes)

				if len(result_clustering.clusters[i]) > 0:
					for object_num in result_clustering.clusters[i]:
						for attr_num in attributes:
							attr_averages[attr_num] += data[object_num][attr_num]
					
					for attr_num in attributes:
						attr_averages[attr_num] /= len(result_clustering.clusters[i])
					
					result_clustering.centroids[i] = attr_averages
		
		print "kmeans finished after %d iterations" % t
		
		return result_clustering


iris_data, iris_keys = data.iris()

summary_stats = None

#for euclidean
optimal_clustering = 0
minimal_sse = 9999
all_clusterings = []

for t in range(20):

	i = 3

	new_clustering = clustering.kmeans(iris_data, k=i, distance=distance.euclidean, prototype=prototype.avg)

	if summary_stats == None:
		summary_stats = new_clustering.source_data_summary()

	print "iris statistics:"
	print summary_stats

	print "kmeans result clusters based on euclidean distance for k = %d (trial %d):" % (i, t)


	new_clustering.describe()

	current_sse = new_clustering.total_sse()

	if(current_sse < minimal_sse):
		optimal_clustering = t
		minimal_sse = current_sse

	all_clusterings.append(new_clustering)


print "optimal clustering:"
all_clusterings[optimal_clustering].describe()