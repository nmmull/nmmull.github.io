import unittest
import numpy as np
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from hw05progsol import nums_to_matrix, encode, decode, nums_to_message

key_1 = np.array(
    [[0., 0, 1, 1],
     [1, 0, 1, 1],
     [0, 1, 1, 1],
     [0, 0, 1, 0]])

key_2 = np.array(
    [[0., 1, 1, 1],
     [1, 1, 1, 0],
     [0, 1, 0, 0],
     [1, 1, 0, 0]])

message = "AMESSAGEWITHWORDS"
code = "C1--+9!3CR)?CV/Eog;M"

class TestSubmission(unittest.TestCase):

    @weight(2)
    def test_nums_to_matrix_basic_1(self):
        a = np.array([[1, 2, 3, 4]]).T
        self.assertTrue(np.array_equal(nums_to_matrix([1, 2, 3, 4]), a))

    @weight(2)
    def test_nums_to_matrix_basic_2(self):
        a = np.array(
            [[1, 3, 2, -1],
             [0, 0, 12, 0]]).T
        b = [1, 3, 2, -1, 0, 0, 12, 0]
        self.assertTrue(np.array_equal(nums_to_matrix(b), a))

    @weight(2)
    @visibility("after_due_date")
    def test_nums_to_matrix(self):
        a = np.random.rand(24)
        m = np.copy(a)
        m.shape = (6, 4)
        self.assertTrue(np.array_equal(nums_to_matrix(list(a)), m.T))

    @weight(2)
    def test_encode_basic(self):
        self.assertEqual(encode(key_2, message), code)

    @weight(2)
    def test_decode_basic(self):
        self.assertEqual(decode(key_2, code), message)

    @weight(3)
    @visibility("after_due_date")
    def test_full(self):
        for _ in range(10):
            s = np.random.randint(0, 26, 100)
            m = nums_to_message(s)
            c = encode(key_1, m)
            self.assertNotEqual(m, c)
            self.assertEqual(decode(key_1, c), m)
