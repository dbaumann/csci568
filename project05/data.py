import arff

def iris():
	name, is_sparse, attributes, data = arff.arffread(open('iris.arff', 'rb'))

	return ([[float(value) for value in row[0:4]] for row in data],
			[attributes[0][0], attributes[1][0], attributes[2][0], attributes[3][0]])