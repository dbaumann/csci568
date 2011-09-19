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

suite = unittest.TestLoader().loadTestsFromTestCase(TestSimilarityMetrics)
unittest.TextTestRunner(verbosity=2).run(suite)