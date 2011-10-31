import random

from nodes import *
from layer import layer

INPUT=0
HIDDEN=1
OUTPUT=2

class network:
	"""
	An artificial neural network. Contains a single hidden layer.
	"""
	def __init__(self, input, output, hidden_count=2, activation_function=lambda x: 1.0-x*x):
		self.activation_function = activation_function

		#set up layers
		self.layers = []
		self.layers.insert(INPUT, layer([input_node(val) for val in input]))
		self.layers.insert(HIDDEN, layer([active_node(0.0)]*hidden_count))
		self.layers.insert(OUTPUT, layer([active_node(val) for val in output]))

		#set up weights
		self.weights = []
		self.weights.insert(INPUT, [
			[random.randint(-1,1) for val in self.layers[HIDDEN]]
				for val in self.layers[INPUT]
		])
		self.weights.insert(HIDDEN, [
			[random.randint(-1,1) for val in self.layers[OUTPUT]]
				for val in self.layers[HIDDEN]
		])

	def __get_weight(self, origin_layer, from_node, to_node):
		return self.weights[origin_layer][from_node][to_node]

	def __set_weight(self, origin_layer, from_node, to_node, value):
		self.weights[origin_layer][from_node][to_node] = value

net = network([1,2,3],[4,5,6])
