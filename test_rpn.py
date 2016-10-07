import unittest

import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculator("1 1 +")
		self.assertEqual(2, result)
