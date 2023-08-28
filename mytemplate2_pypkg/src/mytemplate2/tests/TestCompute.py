"""
"""

import unittest

import mytemplate2 as myt2


class TestCompute(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSomething(self):
        self.assertEqual(-250.0, myt2.compute(5.0))
