import unittest
import numpy as np
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
import hw08progsol as hw

part_a = np.eye(8)
part_b = 4 * np.eye(8)
part_c = np.eye(8, k=1)
part_d = np.diag(np.arange(1., 9))
part_e = 2 * np.diag(np.arange(1., 9)) + np.eye(8, k=1) + 3 * np.eye(8, k=-1)
part_f = np.diag(np.arange(8., 0, -1)) + np.diag(np.arange(1., 8), k=1)
part_g = np.zeros((8, 8))
part_h = 2 * np.ones((8, 8))
part_i = np.hstack((3 * np.ones((4, 4)), np.eye(4)))
part_j = np.vstack((np.hstack((np.ones((4, 5)), np.zeros((4, 3)))), np.hstack((np.eye(4), -2 * np.ones((4, 4))))))
part_k = np.eye(8)[:,[4, 1, 4, 6]]
part_l = np.eye(8)[range(7, -1, -1)]
part_m = np.tril(2 * np.ones((8, 8)))

class TestSubmission(unittest.TestCase):

    @weight(1)
    def test_part_a(self):
        self.assertTrue(np.allclose(part_a, hw.part_a))

    @weight(1)
    def test_part_b(self):
        self.assertTrue(np.allclose(part_b, hw.part_b))

    @weight(1)
    def test_part_c(self):
        self.assertTrue(np.allclose(part_c, hw.part_c))

    @weight(1)
    def test_part_d(self):
        self.assertTrue(np.allclose(part_d, hw.part_d))

    @weight(1)
    @visibility("after_due_date")
    def test_part_e(self):
        self.assertTrue(np.allclose(part_e, hw.part_e))

    @weight(1)
    @visibility("after_due_date")
    def test_part_f(self):
        self.assertTrue(np.allclose(part_f, hw.part_f))

    @weight(1)
    @visibility("after_due_date")
    def test_part_g(self):
        self.assertTrue(np.allclose(part_g, hw.part_g))

    @weight(1)
    @visibility("after_due_date")
    def test_part_h(self):
        self.assertTrue(np.allclose(part_h, hw.part_h))

    @weight(1)
    @visibility("after_due_date")
    def test_part_i(self):
        self.assertTrue(np.allclose(part_i, hw.part_i))

    @weight(1)
    @visibility("after_due_date")
    def test_part_j(self):
        self.assertTrue(np.allclose(part_j, hw.part_j))

    @weight(1)
    @visibility("after_due_date")
    def test_part_k(self):
        self.assertTrue(np.allclose(part_k, hw.part_k))

    @weight(1)
    @visibility("after_due_date")
    def test_part_l(self):
        self.assertTrue(np.allclose(part_l, hw.part_l))

    @weight(1)
    @visibility("after_due_date")
    def test_part_m(self):
        self.assertTrue(np.allclose(part_m, hw.part_m))
