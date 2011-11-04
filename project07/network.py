import random
import math

from nodes import *
from layer import layer

INPUT=0
HIDDEN=1
OUTPUT=2

class network:
    """
    An artificial neural network. Contains a single hidden layer.
    The sizes of the input and output layers are determined from those of the input and output parameters.
    """

    def __init__(self, input, output, hidden_count=2, activation_function=math.tanh):
        self.activation_function = activation_function

        #set up layers
        self.layers = []
        self.layers.insert(INPUT, layer([input_node(val) for val in input]))
        self.layers.insert(HIDDEN, layer([active_node(0.0)]*hidden_count))
        self.layers.insert(OUTPUT, layer([active_node(val) for val in output]))

        #set up weights - [layer id][from node id][to node id] = random initial weight in [-1,1]
        self.weights = []
        self.weights.insert(INPUT, [
            [random.triangular(-1,1) for tuple in self.layers[HIDDEN]]
                for val in self.layers[INPUT]
        ])
        self.weights.insert(HIDDEN, [
            [random.triangular(-1,1) for tuple in self.layers[OUTPUT]]
                for val in self.layers[HIDDEN]
        ])

    def feed_forward(self):
        """
        Propagate the values of the input nodes through the network.
        @return list: values of the output nodes
        """
        
        input_results = [node.activate() for (i, node) in self.layers[INPUT]]

        transposed_weights = zip(*self.weights[INPUT])

        print "feeding forward:"

        print "\ninput values:"
        print input_results

        print "\ninput weights:"
        print(self.weights[INPUT])

        print "\ntransposed input weights:"
        print transposed_weights

        hidden_results = [node.activate(input_results, transposed_weights[i], self.activation_function)
            for (i, node) in self.layers[HIDDEN]]

        transposed_weights = zip(*self.weights[HIDDEN])

        print "\nhidden values:"
        print hidden_results

        print "\nhidden weights:"
        print(self.weights[HIDDEN])

        print "\ntransposed hidden weights:"
        print transposed_weights

        output_results = [node.activate(hidden_results, transposed_weights[i], self.activation_function)
            for (i, node) in self.layers[OUTPUT]]

        print "\nfeed forward output:"
        print output_results

        return output_results
