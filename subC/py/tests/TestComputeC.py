"""
"""

import unittest

import mytemplate2.subC as myt2C


class TestComputeC(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSomething(self):
        self.assertEqual(27.0, myt2C.compute_c(3.0))
