"""
"""

import unittest

import mytemplate.subB as mytB


class TestComputeB(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSomething(self):
        self.assertEqual(27.0, mytB.compute_b(3.0))
