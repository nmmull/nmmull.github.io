import unittest
import numpy as np
import scipy as sp
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from hw10progsol import *

basic = np.array([
    [0.,  0, 1/3, 0,   0,   0],
    [1/2, 0, 1/3, 0,   0,   0],
    [1/2, 0, 0,   0,   0,   0],
    [0,   0, 0,   0,   1/2, 1],
    [0,   0, 1/3, 1/2, 0,   0],
    [0,   0, 0,   1/2, 1/2, 0]])

basic2 = np.array([
    [0.,  1/6, 1/3, 0,   0,   0],
    [1/2, 1/6, 1/3, 0,   0,   0],
    [1/2, 1/6, 0,   0,   0,   0],
    [0,   1/6, 0,   0,   1/2, 1],
    [0,   1/6, 1/3, 1/2, 0,   0],
    [0,   1/6, 0,   1/2, 1/2, 0]])

rw_size = 800000
rw_off_diag1 = np.ones(rw_size - 1) / 2
rw_off_diag1[0] = 0
rw_off_diag2 = np.ones(rw_size - 1) / 2
rw_off_diag2[-1] = 0
rand_walk = sp.sparse.diags([rw_off_diag1, rw_off_diag2], [-1, 1], format='csc')
rw_zeros = np.zeros(rw_size)
rw_zeros[0] = 1
rw_zeros[-1] = 1

top_ten_stanford = [281, 67, 1352, 4898, 3367, 341, 445, 443, 474, 1350]
top_ten_berkstan = [288238, 9, 225465, 54130, 1283, 564114, 288346, 65122, 113, 114]

class TestSubmission(unittest.TestCase):

    @weight(2)
    def test_power_step_basic_1(self):
        """Tests a single call of power_step with alpha=0"""
        v = np.ones(6) / 6
        zeros = np.eye(6)[1]
        alpha = 0
        one_step = power_step(basic, v, zeros, 0)
        one_step2 = basic2 @ v
        self.assertTrue(np.allclose(one_step, one_step2))

    @weight(2)
    @visibility("after_due_date")
    def test_power_step_basic_2(self):
        """Tests a single call of power_step with alpha = 1"""
        v = np.ones(6) / 6
        one_step = power_step(basic, v, np.zeros(6), 1)
        self.assertTrue(np.allclose(one_step, np.ones(6) / 6))

    @weight(2)
    @visibility("after_due_date")
    def test_power_step_basic_3(self):
        """Tests a single call of power_step with alpha=0.15"""
        v = np.ones(6) / 6
        zeros = np.eye(6)[1]
        one_step = power_step(basic, v, zeros)
        one_step2 = 0.85 * basic2 @ v + 0.15 / 6
        self.assertTrue(np.allclose(one_step, one_step2))

    @weight(2)
    def test_power_step_random(self):
        """Tests power_step on 5 random matrices of size (100,100)"""
        rng = np.random.default_rng(12345)
        for _ in range(5):
            a = np.eye(100) + rng.integers(2, size=(100,100))
            v = rng.integers(2, size=100)
            for i in range(100):
                a[:,i] /= np.sum(a[:,i])
            one_step = power_step(a, v, np.zeros(100))
            one_step2 = 0.85 * a @ v + 0.15 / 100 * np.sum(v)
            self.assertTrue(np.allclose(one_step, one_step2))

    @weight(4)
    def test_power_step_large_1(self):
        """Tests power_step on a very large matrix (so you don't build the all-ones matrix explicitly)"""
        size = 800000
        a = sp.sparse.eye(size, format='csc')
        v = np.ones(size)
        one_step = power_step(a, v, np.zeros(size))
        self.assertTrue(np.allclose(one_step, v))

    @weight(4)
    @visibility("after_due_date")
    def test_power_step_large_2(self):
        """Tests power_step on a very large random walk matrix (so you don't build the all-ones matrix explicitly)"""
        v = np.ones(rw_size)
        one_step = power_step(rand_walk, v, rw_zeros)
        one_step2 = 0.85 * rand_walk.dot(v) + 0.85 * 2 / rw_size + 0.15
        self.assertTrue(np.allclose(one_step, one_step2))

    @weight(2)
    def test_l1_error_basic(self):
        """Tests l1_error on a basic input"""
        u = np.ones(10)
        v = np.ones(10) * (-0.5)
        self.assertTrue(np.isclose(l1_error(u, v), 15))

    @weight(2)
    @visibility("after_due_date")
    def test_l1_error_random(self):
        """Tests l1_error on 20 random inputs"""
        rng = np.random.default_rng(20348)
        for _ in range(20):
            v = rng.random(10000)
            u = rng.random(10000)
            self.assertTrue(np.isclose(l1_error(u, v), np.sum(np.abs(u - v))))
        return None

    @weight(2)
    def test_power_iter_basic_1(self):
        """Tests power_iter on a basic matrix"""
        out = power_iter(basic2, np.ones(6), np.zeros(6))
        next_step = power_step(basic2, out, np.zeros(6))
        self.assertFalse(np.allclose(out, np.ones(6)))
        self.assertTrue(l1_error(out, next_step) <= 0.001)

    @weight(2)
    @visibility("after_due_date")
    def test_power_iter_basic_2(self):
        """Tests power_iter on two equivalent matrices"""
        start = np.ones(6)
        zeros = np.eye(6)[1]
        out = power_iter(basic, start, zeros)
        out2 = power_iter(basic2, start, np.zeros(6))
        self.assertFalse(np.allclose(out, start))
        self.assertFalse(np.allclose(out2, start))
        self.assertTrue(np.allclose(out, out2))

    @weight(4)
    def test_power_iter_large(self):
        """Tests power_iter on a very large random walk"""
        start = np.zeros(rw_size)
        start[0] = 1.0
        out = power_iter(rand_walk, start, rw_zeros)
        self.assertFalse(np.allclose(out, start))
        next_step = power_step(rand_walk, out, rw_zeros)
        self.assertTrue(np.sum(np.abs(out - next_step)) <= 0.001)
        self.assertTrue(np.isclose(np.sum(out), 1.0))

    @weight(0)
    def test_top_five_stanford(self):
        """Checks top 5 for the Stanford data set"""
        self.assertEqual(top_five_stanford, [281, 67, 1352, 4898, 3367])

    @weight(0)
    def test_top_five_berkstan(self):
        """Checks top 5 for the Berkeley-Stanford data set"""
        self.assertEqual(top_five_berkstan, [288238, 9, 225465, 54130, 1283])

    @weight(0)
    @visibility("after_due_date")
    def test_top_five_google(self):
        """Checks top 5 for the Google data set"""
        self.assertEqual(top_five_google, [115, 2138, 2560, 3178, 1950])

    @weight(6)
    @visibility("after_due_date")
    def test_full_stanford(self):
        """Verifies your computation on the Stanford dataset"""
        f = open('web-Stanford.npy', 'rb')
        ranks = np.load(f)
        f.close()
        self.assertTrue(np.allclose(np.argsort(ranks)[:-11:-1], top_ten_stanford))

    @weight(6)
    @visibility("after_due_date")
    def test_full_berkstan(self):
        """Verifies your computation on the Stanford-Berkeley dataset"""
        f = open('web-BerkStan.npy', 'rb')
        ranks = np.load(f)
        f.close()
        self.assertTrue(np.allclose(np.argsort(ranks)[:-11:-1], top_ten_berkstan))
