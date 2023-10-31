import unittest
import numpy as np
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from hw06progsol import random_walk, adjacency_to_stochastic

class TestSubmission(unittest.TestCase):

    @weight(3)
    def test_a_to_s_basic_1(self):
        a = np.ones((10, 10))
        b = np.copy(a)
        adjacency_to_stochastic(b)
        self.assertTrue(np.allclose(a / 10, b))

    @weight(3)
    def test_a_to_s_basic_zeros(self):
        a = np.zeros((10, 10))
        b = np.copy(a)
        adjacency_to_stochastic(b)
        self.assertTrue(np.allclose(a, b))

    @weight(6)
    def test_r_w(self):
        a = np.ones((10, 10)) / 10
        for i in range(10):
            walk = random_walk(a, i, 100)
            self.assertEqual(len(walk), 100)
            self.assertEqual(walk[0], i)
