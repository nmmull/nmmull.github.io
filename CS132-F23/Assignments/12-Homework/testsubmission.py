import unittest
import numpy as np
import scipy as sp
import math
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from hw12progsol import *

class TestSubmission(unittest.TestCase):

    @weight(4)
    def test_dist_basic(self):
        """Basic test of distance function"""
        u = np.zeros(100)
        v = np.ones(100)
        self.assertTrue(np.isclose(dist(u, v), 10))

    @weight(6)
    @visibility("after_due_date")
    def test_dist_full(self):
        """Full test of distance function"""
        rng = np.random.default_rng(2424)
        for _ in range(100):
            u = rng.random(100)
            v = rng.random(100)
            self.assertTrue(np.isclose(dist(u, v), np.linalg.norm(u - v)))

    @weight(4)
    def test_linear_design_matrix_shape(self):
        """Verify that the linear design matrix is the correct shape"""
        rng = np.random.default_rng(1001)
        for _ in range(100):
            r = rng.integers(1,100)
            c = rng.integers(1,100)
            a = rng.random((r, c))
            d = linear_design_matrix(a)
            self.assertEqual(d.shape[0], r)
            self.assertEqual(d.shape[1], c + 1)

    @weight(6)
    def test_linear_design_matrix_basic(self):
        """Basic test of the linear_design_matrix function"""
        inp = np.array([
            [0, -5],
            [1, 1],
            [2, -2]])
        out = np.array([
            [1, 0, -5],
            [1, 1, 1],
            [1, 2, -2]])
        sol = linear_design_matrix(inp)
        for i in range(out.shape[1]):
            has_col = False
            for j in range(sol.shape[1]):
                if np.allclose(out[:,i], sol[:,j]):
                    has_col = True
                    break
            self.assertTrue(has_col)

    @weight(10)
    @visibility("after_due_date")
    def test_linear_design_matrix_full(self):
        """Full test of the linear_design_matrix_function"""
        rng = np.random.default_rng(3232)
        for _ in range(10):
            r = rng.integers(1, 100)
            c = rng.integers(1, 100)
            a = rng.random((r, c))
            obs = rng.random(r)
            d = linear_design_matrix(a)
            pred = d @ np.linalg.lstsq(d, obs, rcond=None)[0]
            test = np.column_stack((a, np.ones(r)))
            actual = test @ np.linalg.lstsq(test, obs, rcond=None)[0]
            self.assertTrue(np.allclose(pred, actual))

    @weight(4)
    def test_quadratic_design_matrix_shape(self):
        """Verify that the quadratic design matrix is the correct shape"""
        rng = np.random.default_rng(2322)
        for _ in range(100):
            r = rng.integers(1,100)
            c = rng.integers(1,100)
            a = rng.random((r, c))
            d = quadratic_design_matrix(a)
            self.assertEqual(d.shape[0], r)
            self.assertEqual(d.shape[1], math.comb(c + 2, c))

    @weight(6)
    def test_quadratic_design_matrix_basic(self):
        """Basic test of the quadratic_design_matrix function"""
        inp = np.array([
            [0, -5],
            [1, 1],
            [2, -2]])
        out = np.array([
            [1, 0, -5, 0, 0, 25],
            [1, 1, 1, 1, 1, 1],
            [1, 2, -2, -4, 4, 4]])
        sol = quadratic_design_matrix(inp)
        for i in range(out.shape[1]):
            has_col = False
            for j in range(sol.shape[1]):
                if np.allclose(out[:,i], sol[:,j]):
                    has_col = True
                    break
            self.assertTrue(has_col)

    @weight(10)
    @visibility("after_due_date")
    def test_quadratic_design_matrix_full(self):
        """Full test of the quadratic_design_matrix_function"""
        rng = np.random.default_rng(2310)
        for _ in range(10):
            r = rng.integers(1, 50)
            c = rng.integers(1, 50)
            a = rng.random((r, c))
            obs = rng.random(r)
            d = quadratic_design_matrix(a)
            pred = d @ np.linalg.lstsq(d, obs, rcond=None)[0]
            test = np.column_stack((a, np.ones(r)))
            for i in range(c):
                for j in range(i, c):
                    test = np.column_stack((a[:,i] * a[:,j], test))
            actual = test @ np.linalg.lstsq(test, obs, rcond=None)[0]
            self.assertTrue(np.allclose(pred, actual))

    @weight(3)
    def test_cubic_design_matrix_shape(self):
        """Verify that the cubic design matrix is the correct shape"""
        rng = np.random.default_rng(1031)
        for _ in range(100):
            r = rng.integers(1,10)
            c = rng.integers(1,10)
            a = rng.random((r, c))
            d = cubic_design_matrix(a)
            self.assertEqual(d.shape[0], r)
            self.assertEqual(d.shape[1], math.comb(c + 3, c))

    @weight(5)
    def test_cubic_design_matrix_basic(self):
        """Basic test of the linear_design_matrix function"""
        inp = np.array([
            [0, -5],
            [1, 1],
            [2, -2]])
        out = np.array([
            [1, 0, -5,  0, 0, 25, 0, -125, 0, 0],
            [1, 1,  1,  1, 1,  1, 1, 1, 1, 1],
            [1, 2, -2, -4, 4,  4, 8, -8, 8, -8]] )
        sol = cubic_design_matrix(inp)
        for i in range(out.shape[1]):
            has_col = False
            for j in range(sol.shape[1]):
                if np.allclose(out[:,i], sol[:,j]):
                    has_col = True
                    break
            self.assertTrue(has_col)

    @weight(10)
    @visibility("after_due_date")
    def test_cubic_design_matrix_full(self):
        """Full test of the quadratic_design_matrix_function"""
        rng = np.random.default_rng(2310)
        for _ in range(10):
            r = rng.integers(1, 10)
            c = rng.integers(1, 10)
            a = rng.random((r, c))
            obs = rng.random(r)
            d = cubic_design_matrix(a)
            pred = d @ np.linalg.lstsq(d, obs, rcond=None)[0]
            test = np.column_stack((a, np.ones(r)))
            for i in range(c):
                for j in range(i, c):
                    test = np.column_stack((a[:,i] * a[:,j], test))
            for i in range(c):
                for j in range(i, c):
                    for k in range(j, c):
                        test = np.column_stack((a[:,i] * a[:,j] * a[:,k], test))
            actual = test @ np.linalg.lstsq(test, obs, rcond=None)[0]
            self.assertTrue(np.allclose(pred, actual))
