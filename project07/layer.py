class layer:
    """
    A layer in an artificial neural network, which may consist of any number of nodes.
    """

    def __init__(self, nodes):
        self.nodes = list(nodes)

    def __getitem__(self, key):
        return self.nodes[key]

    def __setitem__(self, key, value):
        """
        @raises IndexError: when a node with the suggested key doesn't exist
        @raises TypeError:  when passed a value that doesn't behave like a node ought to
        """
        
        #make sure the item being set can actually be activated, but don't activate:
        if('activate' not in dir(value)):
            raise TypeError("Attempted to add an object to layer that can't be activated.")

        self.nodes[key] = value

    def __iter__(self):
        for i in range(len(self.nodes)): yield (i, self.nodes[i])

    def __len__(self):
        return len(self.nodes)