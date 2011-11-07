import network

net = network.network([1, 0.25, -0.5],[1, -1, 0])

it = net.training_iterator(training_goal=0.03, history_size=10)
it.send(None)

training_data = [([1, 0.25, -0.5], [1, -1, 0], 0.5)]*100

try:
	for row in training_data:
		it.send(row)
except StopIteration:
	print "training goal reached"

