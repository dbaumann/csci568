class layer:
	"""
	A layer in an artificial neural network which may consist of any
	number of nodes.
	"""

	def __init__(self, nodes):
		self.nodes = list(nodes)

	def __getitem__(self, key):
		return self.nodes[key]

	def __setitem__(self, key, value):
		"""
		@raises IndexError: when a node with a particular key doesn't exist
		"""
		self.nodes[key] = value

	def __iter__(self):
		for node in self.nodes: yield node