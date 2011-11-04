class input_node:
    """A static neuron that always contains the same information."""

    def __init__(self, value):
        self.output = value

    def activate(self):
        return self.output

class active_node:
    """A dynamic neuron."""

    def __init__(self, value):
        self.output = value

    def activate(self, inputs, weights, activation_function):
        """
        @param inputs: sequence of n input values
        @param weights: sequence of n weights, one for each input value
        @param activation_function: sigmoid function used in calculation of output
        """
        self.output = activation_function(self.__dot_product(inputs, weights))
        return self.output

    def __dot_product(self, vector1, vector2):
        """
        @raises ValueError: if arguments don't have same length
        """
        if(len(vector1) != len(vector2)):
            raise ValueError("Dot product arguments should have same length.")

        return sum(vector1[i]*vector2[i] for i in range(len(vector1)))