#!/usr/bin/env python3

from study import rearrange_name
import unittest

class TestingRearrangeName(unittest.TestCase):
	def test_basic(self):
		testcase = 'Lovelace, Ada'
		expected = 'Ada Lovelace'
		self.assertEqual(rearrange_name(testcase), expected)

unittest.main()	

