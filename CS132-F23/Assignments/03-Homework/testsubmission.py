import unittest
import numpy as np
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from hw03progsol import *

X = np.array(
    [[1., 0, 0, 3],
     [0, 1, 0, 2],
     [0, 0, 1, -3]])
X[0] += 2 * X[1] - 3 * X[2]
X[1] += X[0] + X[2]
X[2] += -3 * X[1] + 2 * X[0]
b = X.T[-1]
a = X.T[:-1].T

Y = np.array(
    [[1., 0, 0, 1],
     [0, 1, 0, 2],
     [0, 0, 0, 3]])
Y[0] += 2 * Y[1] + 3 * Y[2]
Y[1] -= 3 * Y[0] + 5 * Y[2]
Y[2] += Y[0] + Y[1]
d = Y.T[-1]
c = Y.T[:-1].T

class TestIsConsistent(unittest.TestCase):

    @weight(2)
    @number("1")
    @visibility("after_due_date")
    def test_consistent_mat_true(self):
        """Check consistent matrix equation"""
        try:
            self.assertTrue(is_consistent_mat_eq(a, b))
        except:
            self.fail("error in is_inconsisent_mat_eq")

    @weight(2)
    @number("2")
    @visibility("after_due_date")
    def test_consistent_mat_false(self):
        """Check inconsistent matrix equation"""
        try:
            self.assertFalse(is_consistent_mat_eq(c, d))
        except:
            self.fail("error in is_consistent_mat_eq")

    @weight(1)
    @number("3")
    @visibility("after_due_date")
    def test_consistent_vec_true(self):
        """Check consistent vector equation"""
        try:
            self.assertTrue(is_consistent_vec_eq(vecs_of_mat(a), b))
        except:
            self.fail("error in is_consistent_vec_eq")

    @weight(1)
    @number("4")
    @visibility("after_due_date")
    def test_consistent_vec_false(self):
        """Check inconsistent vector equation"""
        try:
            self.assertFalse(is_consistent_vec_eq(vecs_of_mat(c), d))
        except:
            self.fail("error in is_consistent_vec_eq")

    @weight(2)
    @number("5")
    @visibility("after_due_date")
    def test_in_span_true(self):
        """Check in span"""
        try:
            self.assertTrue(in_span(b, vecs_of_mat(a)))
        except:
            self.fail("error in in_span")

    @weight(2)
    @number("6")
    @visibility("after_due_date")
    def test_in_span_false(self):
        """Check not in span"""
        try:
            self.assertFalse(in_span(d, vecs_of_mat(c)))
        except:
            self.fail("error in in_span")

    @weight(2)
    @number("7")
    @visibility("after_due_date")
    def test_num_of_pivots(self):
        """Check number of pivots"""
        try:
            self.assertEqual(num_of_pivots(a), 3)
        except:
            self.fail("""error in num_of_pivots""")

    @weight(2)
    @number("8")
    @visibility("after_due_date")
    def test_num_of_pivots2(self):
        """Check number of pivots in inconsistent system"""
        try:
            self.assertEqual(num_of_pivots(c), 2)
        except:
            self.fail("""error in num_of_pivots""")

    @weight(1)
    @number("9")
    @visibility("after_due_date")
    def test_full_span_true(self):
        """Check full span vectors"""
        try:
            self.assertTrue(full_span_cols(a))
        except:
            self.fail("""error in full_span_cols""")

    @weight(1)
    @number("10")
    @visibility("after_due_date")
    def test_full_span_false(self):
        """Check not full span vectors"""
        try:
            self.assertFalse(full_span_cols(c))
        except:
            self.fail("""error in full_span_cols""")

    @weight(1)
    @number("11")
    @visibility("after_due_date")
    def test_lin_ind_true(self):
        """Check linearly independent columns"""
        try:
            self.assertTrue(lin_ind_cols(a))
        except:
            self.fail("""error in lin_ind_cols""")

    @weight(1)
    @number("12")
    @visibility("after_due_date")
    def test_lin_ind_false(self):
        """Check linearly dependent columns"""
        try:
            self.assertFalse(lin_ind_cols(c))
        except:
            self.fail("""error in full_span_cols""")
