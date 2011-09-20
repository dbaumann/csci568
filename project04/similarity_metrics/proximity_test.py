import proximity
import unittest

from math import sqrt

class TestSimilarityMetrics(unittest.TestCase):

	def test_euclidean(self):
		vector1 = vector2 = [1, 2, 3]
		expected = 1
		self.assertEqual(expected, proximity.euclidean(vector1, vector2))

		vector2 = [4, 5, 6]
		expected = 1/(1+sqrt(27))
		self.assertEqual(expected, proximity.euclidean(vector1, vector2))

	def test_smc(self):
		self.__confirm_binary_restriction(proximity.smc)

		vector1 = [1, 0, 0, 1, 1]

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
		self.__confirm_binary_restriction(proximity.jaccard)
		
		vector1 = [1, 0, 0, 1, 1]

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

	def test_pearson(self):
		vector1 = [1, 2, 3, 4]

		vector2 = vector1
		expected = 1
		self.assertAlmostEqual(expected, proximity.pearson(vector1, vector2))

		vector2 = [4, 3, 2, 1]
		expected = -1
		self.assertAlmostEqual(expected, proximity.pearson(vector1, vector2))

		vector2 = [5, 9, 11, 2]
		expected = -.224179415
		self.assertAlmostEqual(expected, proximity.pearson(vector1, vector2))

	def test_cosine(self):
		vector1 = [1, 2, 3]

		vector2 = vector1
		expected = 1
		self.assertAlmostEqual(expected, proximity.cosine(vector1, vector2))

		vector2 = [-4, 8, -4]
		expected = 0
		self.assertAlmostEqual(expected, proximity.cosine(vector1, vector2))

		vector2 = [5, 6, 1]
		expected = 0.678844233302
		self.assertAlmostEqual(expected, proximity.cosine(vector1, vector2))

	def __confirm_binary_restriction(self, function):
		self.assertRaises(ValueError, function, [1, 0, 0, 1, -1], [1, 0, 0, 1, -1])
		self.assertRaises(ValueError, function, [1, 0, 0, 1, 2], [1, 0, 0, 1, 2])



	

suite = unittest.TestLoader().loadTestsFromTestCase(TestSimilarityMetrics)
unittest.TextTestRunner(verbosity=2).run(suite)