"""
"""

import unittest

import mytemplate as myt


class TestCompute(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSomething(self):
        self.assertEqual(25.0, myt.compute(5.0))
