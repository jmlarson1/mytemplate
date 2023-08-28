"""
"""

import unittest

import numpy as np

from pathlib import Path

import mytemplate.subA as mytA

_TEST_PATH = Path(__file__).resolve().parent


class TestComputeA(unittest.TestCase):
    def setUp(self):
        fname = _TEST_PATH.joinpath("compute_a_test_data.csv")
        self.__tests = np.loadtxt(fname, delimiter=",")

    def testSomething(self):
        self.assertTrue(len(self.__tests) > 0)

        for x, expected in self.__tests:
            self.assertAlmostEqual(expected, mytA.compute_a(x), places=15)
