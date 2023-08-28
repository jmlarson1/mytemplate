"""
"""

import unittest

import numpy as np

from pathlib import Path

import mytemplate as myt

_TEST_PATH = Path(__file__).resolve().parent


class TestCompute(unittest.TestCase):
    def setUp(self):
        fname = _TEST_PATH.joinpath("compute_test_data.csv")
        self.__tests = np.loadtxt(fname, delimiter=",")

    def testSomething(self):
        self.assertTrue(len(self.__tests) > 0)

        for x, expected in self.__tests:
            self.assertEqual(expected, myt.compute(x))

    def testConfig(self):
        # This shouldn't be in this test case in a real package
        self.assertListEqual([1.1, 2.2, 3.3, 4.4, 5.5], myt.config)
