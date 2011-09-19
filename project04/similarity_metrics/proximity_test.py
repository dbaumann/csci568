import proximity
import unittest

from math import sqrt

class TestSimilarityMetrics(unittest.TestCase):

	def test_euclidean(self):
		vector1 = vector2 = [1,2,3]
		expected = 1
		self.assertEqual(expected, proximity.euclidean(vector1, vector2))

		vector2 = [4,5,6]
		expected = 1/(1+sqrt(27))
		self.assertEqual(expected, proximity.euclidean(vector1, vector2))

	def test_smc(self):
		vector1 = [1, 0, 0, 1, 1]

		#should only accept vectors of binary values
		self.assertRaises(ValueError, proximity.smc, vector1, [1, 0, 0, 1, -1])
		self.assertRaises(ValueError, proximity.smc, vector1, [1, 0, 0, 1, 2])

		vector2 = vector1
		expected = 1
		self.assertEqual(expected, proximity.smc(vector1, vector2))

		vector2 = [0, 1, 1, 0, 0]
		expected = 0
		self.assertEqual(expected, proximity.smc(vector1, vector2))

		vector2 = [1, 1, 1, 1, 1]
		expected = 3/5.0
		self.assertEqual(expected, proximity.smc(vector1, vector2))

	def test_jaccard(self):
		vector1 = [1, 0, 0, 1, 1]

		#should only accept vectors of binary values
		self.assertRaises(ValueError, proximity.jaccard, vector1, [1, 0, 0, 1, -1])
		self.assertRaises(ValueError, proximity.jaccard, vector1, [1, 0, 0, 1, 2])

		vector2 = vector1
		expected = 1
		self.assertEqual(expected, proximity.jaccard(vector1, vector2))

		vector2 = [0, 1, 1, 0, 0]
		expected = 0
		self.assertEqual(expected, proximity.jaccard(vector1, vector2))

		vector2 = [1, 1, 1, 1, 1]
		expected = 3/5.0
		self.assertEqual(expected, proximity.jaccard(vector1, vector2))

		vector2 = [0, 0, 1, 1, 1]
		expected = 2/4.0
		self.assertEqual(expected, proximity.jaccard(vector1, vector2))

	

suite = unittest.TestLoader().loadTestsFromTestCase(TestSimilarityMetrics)
unittest.TextTestRunner(verbosity=2).run(suite)