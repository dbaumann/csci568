import sys
import time
from csv import reader, writer

input_file = sys.argv[1]
output_file = sys.argv[2]

file_reader = reader(open(input_file), delimiter=',')
file_writer = writer(open(output_file, 'w'), delimiter=',')

def hamdist(s1, s2):
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

start = time.time()

#read all objects into memory
dataset = []
i = 0
for line in file_reader:
	dataset.append(line[1:])
	# i += 1; if i >= 1000: break

print str(len(dataset)) + " records in " + input_file

#calculate all pairwise distances
distances = [[hamdist(obj1, obj2) for obj1 in dataset] for obj2 in dataset]

print "\ndistance matrix calculated after %f minutes" % (time.time() - start)/60

for line in distances:
	file_writer.writerow(line)

print "\nscript finished in %f minutes" % (time.time() - start)/60