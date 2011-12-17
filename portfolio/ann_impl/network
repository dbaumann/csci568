import random

from nodes import *
from layer import layer

INPUT=0
HIDDEN=1
OUTPUT=2

class network:
    """
    An artificial neural network. Contains a single hidden layer of an arbitrary number of nodes.
    The sizes of the input and output layers are determined from those of the input and output parameters.
    """

    def __init__(self, input, output, hidden_count=2):
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
    
    def refresh_input(self, new_input):
        """
        Refresh the input layer with new nodes.

        @raises     ValueError:     if input list size isn't the same as number of established nodes in input layer
        """
        
        if(len(new_input) != len(self.layers[INPUT])):
            raise ValueError("Attempted to refresh input layer with the wrong number of values.")

        for (i, node) in self.layers[INPUT]:
            self.layers[INPUT][i] = input_node(new_input[i])
    
    def feed_forward(self):
        """
        Propagate the values of the input nodes through the network.

        @return     list:   values of the output nodes
        """

        input_results = [node.activate() for (i, node) in self.layers[INPUT]]

        transposed_input_weights = zip(*self.weights[INPUT])

        hidden_results = [node.activate(input_results, transposed_input_weights[i])
            for (i, node) in self.layers[HIDDEN]]

        transposed_hidden_weights = zip(*self.weights[HIDDEN])

        output_results = [node.activate(hidden_results, transposed_hidden_weights[i])
            for (i, node) in self.layers[OUTPUT]]

        return output_results   

    def training_iterator(self, training_goal, history_size):
        """
        Uses feed-forward back propagation to train the model from data provided as (input, output, learning_rate).
        Iteration stops when output is within <training_goal> of the desired output over the last <history_size> training examples.
        
        @param training_goal    float:  desired accuracy threshold
        @param history_size     int:    number of records to consider when calculating whether the stopping condition has been met
        """

        stopping_cond = False

        delta_avgs = [1.0]*history_size
        icount = 0

        result = [-1]*len(self.layers[OUTPUT])

        while(not stopping_cond):
            (input, output, training_rate) = yield result

            self.refresh_input(input)
            self.feed_forward()

            if(len(output) != len(self.layers[OUTPUT])):
                raise ValueError("Attempted to train with wrong number of output values.")

            #
            # Back-propagate the error
            #

            #calculate error for every node in the output layer by taking the difference between the desired output and the actual output
            for (k, onode) in self.layers[OUTPUT]:
                onode.set_error(output[k] - onode.value())

            #calculate error for every node in the hidden layer by adding together each of the error signals from the output layer, weighted by the strength of the connection
            for (j, hnode) in self.layers[HIDDEN]:
                hnode.set_error(sum(onode.get_error_signal() * self.weights[HIDDEN][j][k] for (k, onode) in self.layers[OUTPUT]))


            #
            # Update weights
            #

            #update each hidden-->output weight by an amount proportional to the product of the output node error signal and the hidden node value
            for (j, hnode) in self.layers[HIDDEN]:
                for (k, onode) in self.layers[OUTPUT]:
                    self.weights[HIDDEN][j][k] += training_rate * onode.get_error_signal() * hnode.value()

            #update each input-->hidden weight by an amount proportional to the product of the hidden node error signal and the input node value
            for (i, inode) in self.layers[INPUT]:
                for (j, hnode) in self.layers[HIDDEN]:
                    self.weights[INPUT][i][j] += training_rate * hnode.get_error_signal() * inode.value()

            result = self.feed_forward()


            #
            # Determine if stopping condition has been met
            #

            delta_avgs[icount % history_size] = sum(abs(output[i] - result[i]) for i in range(len(result)))/len(result)

            icount += 1

            stopping_cond = sum(delta_avgs)/len(delta_avgs) < training_goal

