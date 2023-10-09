import unittest
import numpy as np
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from hw04progsol import inner_product, mat_vec_mult_ip, mat_vec_mult_vs

a = np.array(
        [[1., 2, 3, 4],
         [-2, 3, 0, -2],
         [1, 1, 1, 1]])
x = np.array([1., 0, 2, -1])
u = np.array([1., 2, 3, 4, 5])
v = np.array([-2., 3, 1, -3, 1])

class TestSubmission(unittest.TestCase):

    @weight(2)
    @number("1")
    @visibility("after_due_date")
    def test_inner_product_basic(self):
        try:
            self.assertTrue(np.isclose(inner_product(u, v), np.dot(u, v)))
        except:
            self.fail("Error with inner product")

    @weight(2)
    @number("2")
    @visibility("after_due_date")
    def test_mat_vec_mult_ip_basic(self):
        try:
            self.assertTrue(np.isclose(mat_vec_mult_ip(a, x), a @ x).all())
        except:
            self.fail("Error with mat_vec_mult_ip")

    @weight(2)
    @number("3")
    @visibility("after_due_date")
    def test_mat_vec_mult_vs_basic(self):
        try:
            self.assertTrue(np.isclose(mat_vec_mult_vs(a, x), a @ x).all())
        except:
            self.fail("Error with mat_vec_mult_vs")

    @weight(3)
    @number("4")
    @visibility("after_due_date")
    def test_inner_product(self):
        try:
            for _ in range(1000):
                size = np.random.randint(50)
                u = np.random.rand(size)
                v = np.random.rand(size)
                self.assertTrue(np.isclose(inner_product(u, v), np.dot(u, v)))
        except:
            self.fail("Error with inner product")

    @weight(3)
    @number("5")
    @visibility("after_due_date")
    def test_mat_vec_mult_ip(self):
        try:
            for _ in range(1000):
                row_num = np.random.randint(50)
                col_num = np.random.randint(50)
                a = np.random.rand(row_num, col_num)
                v = np.random.rand(col_num)
                self.assertTrue(np.isclose(mat_vec_mult_ip(a, v), a @ v).all())
        except:
            self.fail("Error with mat_vec_mult_ip")

    @weight(3)
    @number("6")
    @visibility("after_due_date")
    def test_mat_vec_mult_vs(self):
        try:
            for _ in range(1000):
                row_num = np.random.randint(50)
                col_num = np.random.randint(50)
                a = np.random.rand(row_num, col_num)
                v = np.random.rand(col_num)
                self.assertTrue(np.isclose(mat_vec_mult_vs(a, v), a @ v).all())
        except:
            self.fail("Error with mat_vec_mult_vs")
