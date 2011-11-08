import math

import network

def neg_logistic(c, x):
	return c - 1/(1 + math.e**(-x))


net = network.network(input=[1, 3, 5], output=[1, 1, 1], hidden_count=2)

it = net.training_iterator(training_goal=0.03, history_size=10)
it.send(None)

#each row in training set consists of input list, output list, learning rate
training_data = [([1, 0.25, -0.5], [1, -1, 0], neg_logistic(2, n)) for n in range(100)]

try:
	for row in training_data:
		print it.send(row)
except StopIteration:
	print "training goal reached"

