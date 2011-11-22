import re
import math
from csv import reader, writer

#read all objects into memory
data_reader = reader(open("mushroom.data.csv"), delimiter=',')
dataset = []
for line in data_reader:
	dataset.append(line)


#identify objects that are equidistant from both medoids
distances_reader = reader(open("relative_medoid_distances.csv"), delimiter=',')

row_id = re.compile(r'Row[0-9]+')

for line in distances_reader:
	if(row_id.search(line[0]) != None):
		rownum = int(line[0][3:])
		dist1 = float(line[2])
		dist2 = float(line[3])

		if(abs(dist1-dist2) < 0.005):
			print str(rownum+1) + ": " + ",".join(dataset[rownum])
