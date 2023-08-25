"""
"""

import unittest

import mytemplate2.subC as mytC


class TestComputeC(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSomething(self):
        self.assertEqual(9.0, mytC.compute_c(3.0))
