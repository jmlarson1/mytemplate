"""
"""

import unittest

import mytemplate.subA as mytA


class TestComputeA(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSomething(self):
        self.assertEqual(9.0, mytA.compute_a(3.0))
