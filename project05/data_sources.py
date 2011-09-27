import csv

def iris():
	reader = csv.reader(open('iris.csv', 'rb'))

	return ([[float(value) for value in row[0:4]] for row in reader],
			['sepal_length','sepal_width','petal_length','petal_width'])