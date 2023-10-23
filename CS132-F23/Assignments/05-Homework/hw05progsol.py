import numpy as np

"""Mini Hill Cipher

An implementation of a variant of the Hill-Cipher (one which does not
require modular arithmetic)

"""


# HELPER FUNCTIONS

def message_to_nums(s: str) -> list[int]:
    """converts a string to a list of integers that will be encoded

    Parameters:

    s: string to be converted into a list of numbers

    Returns:

    a list of numbers, one for each character, where A is replaced
    with 0, B with 1, and so on

    Example:

    >>> message_to_nums("ABC")
    [0, 1, 2]

    """
    return [ord(c) - 65 for c in s]

def pad(a: list[int]) -> list[int]:
    """pads the end a list of numbers with the number 26 until its
    length is a multiple of 4

    Parameters:

    a: list of ints

    Returns:

    a with 26s padded until len(a) is a multiple of 4

    Example:

    >>> pad([])
    []
    >>> pad([1, 2])
    [1, 2, 26, 26]
    >>> pad([1, 2, 3, 4])
    [1, 2, 3, 4]
    >>> pad([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5, 26, 26, 26]

    """
    if len(a) % 4 != 0:
        return a + [26] * (4 - (len(a) % 4))
    return a

def nums_to_matrix(a: list[int]) -> np.array:
    """re-orients a list of numbers into a matrix

    Parameters:

    a: list of ints

    Preconditions:

    len(a) % 4 == 0 # the length of a is a multiple of 4

    Returns:

    a 2D numpy array whose elements are those of a, and every 4
    elements of a make up a column from top to bottom

    Example:

    >>> nums_to_matrix([1, 2, 3, 4])
    array([[1],
           [2],
           [3],
           [4]])
    >>> nums_to_matrix([1, 2, 3, 4, 5, 6, 7, 8])
    array([[1, 5],
           [2, 6],
           [3, 7],
           [4, 8]])
    >>> nums_to_matrix([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    array([[ 1,  5,  9],
           [ 2,  6, 10],
           [ 3,  7, 11],
           [ 4,  8, 12]])

    """
    assert(len(a) % 4 == 0)
    # >>>>>>>>>>
    a = np.array(a)
    a.shape = len(a) // 4, 4
    return a.T
    # >>>>>>>>>>
    # TODO: fill in this function and change its return value
    return None

def matrix_to_nums(a: np.array) -> list:
    """Turns a matrix back into a list of nums

    Parameters:

    a: 2D numpy array

    Returns:

    list of its elements, flattened along the columns

    Example:

    >>> matrix_to_nums(np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    [1, 5, 9, 2, 6, 10, 3, 7, 11, 4, 8, 12]

    """
    return list(a.flatten('F'))

def nums_to_code(a: list) -> str:
    """Turns an list of numbers into an encoded string"""
    return ''.join([chr(int(i) + 33) for i in a])

def code_to_nums(a: str) -> list[int]:
    """Turns an encoded string into a list of numbers"""
    return [ord(c) - 33 for c in a]

def unpad(a: list[int]) -> list[int]:
    """Removes padding added by pad

    Parameters:

    a: list of ints

    Precondition:

    0 <= a[i] <= 25 for all indices i

    Returns:

    a with padding removed

    Example:

    >>> unpad([1, 2, 3, 4, 26, 26])
    [1, 2, 3, 4]
    >>> unpad([1, 2, 3, 4, 5, 6, 7, 26])
    [1, 2, 3, 4, 5, 6, 7]

    """
    return [x for x in a if x != 26]

def nums_to_message(a: list[int]) -> str:
    """Turns a list of number into a decoded string"""
    return ''.join([chr(int(i) + 65) for i in a])


# FUNCTIONS YOU WILL USE IN YOUR IMPLEMENTATION OF ENCODING AND DECODING

def message_to_matrix(s: str) -> np.array:
    # NOTE: THIS WILL NOT WORK UNTIL YOU'VE IMPLEMENTED num_to_matrix
    return nums_to_matrix(pad(message_to_nums(s)))

def matrix_to_code(a: np.array) -> str:
    return nums_to_code(matrix_to_nums(a))

def code_to_matrix(s: str) -> np.array:
    # NOTE: THIS WILL NOT WORK UNTIL YOU'VE IMPLEMENTED num_to_matrix
    return nums_to_matrix(code_to_nums(s))

def matrix_to_message(a: np.array):
    return nums_to_message(unpad(matrix_to_nums(a)))

# ENCODING AND DECODING

def encode(a: np.array, s: str) -> str:
    """Encodes a string according to the mini-Hill cipher

    Parameters:

    a: 4 by 4 key invertible matrix
    s: string to encode

    Preconditions:

    every character of s is a capital letter of the English alphabet

    Returns:

    s encoded by the mini-Hill cipher

    Example:

    >>> key_1 = np.array(
        [[0., 0, 1, 1],
         [1, 0, 1, 1],
         [0, 1, 1, 1],
         [0, 0, 1, 0]])
    >>> encode(key_1, "THISISASECRET")
    ';NB)3;E!6:82Uho;'

    """
    # >>>>>>>>>>
    mat = message_to_matrix(s)
    encoded = a @ mat
    return matrix_to_code(encoded)
    # >>>>>>>>>>
    # TODO: fill in this function and change its return value
    return None

def decode(a, s):
    """Decodes a string according to the mini-Hill cipher

    Parameters:

    a: key for the mini-Hill cipher
    s: string to decode

    Preconditions:

    s is the result of encoding via the mini-Hill cipher

    Returns:

    s decoded by the mini-Hill cipher

    Example:

    >>> key_1 = np.array(
        [[0., 0, 1, 1],
         [1, 0, 1, 1],
         [0, 1, 1, 1],
         [0, 0, 1, 0]])
    >>> decode(key_1, ";NB)3;E!6:82Uho;")
    'THISISASECRET'

    """
    # >>>>>>>>>>
    mat = code_to_matrix(s)
    decoded = np.linalg.inv(a) @ mat
    return matrix_to_message(decoded)
    # >>>>>>>>>>
    # TODO: fill in this function and change its return value
    return None

# >>>>>>>>>>
def is_invertible(a: np.array):
    """Determines is numpy array is invertible"""
    try:
        np.linalg.inv(a)
        return True
    except:
        return False

def crack(message: str, code: str) -> np.array:
    """Determines the key to a mini-Hill cipher given a message and a
    code, given the first 16 entries of the message form an invertible
    matrix

    Parameters:

    message: str
    code: str

    Returns:

    the key to the mini-Hill cipher user for this encoding, or None if
    the first 16 entries of the message do not form an invertible
    matrix

    Example:

    >>> crack("THISISASECRET", ";NB)3;E!6:82Uho;")
    array([[ 0.,  0.,  1.,  1.],
           [ 1.,  0.,  1.,  1.],
           [ 0.,  1.,  1.,  1.],
           [ 0.,  0.,  1., -0.]])

    """
    # the first 4 columns of the message matrix
    message_mat = nums_to_matrix(pad(message_to_nums(message)))[:,:4]
    code_mat = nums_to_matrix(code_to_nums(code))
    if is_invertible(message_mat):
        key = np.eye(4) # change this line
        key = code_mat @ np.linalg.inv(message_mat)
        return np.rint(key) # round the matrix entries to the nearest int
    return None
# >>>>>>>>>>

# A FEW SIMPLE TEST CASES

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

message = "THISISASECRET"

# code_1 = encode(key_1, message)
# decoded_1 = decode(key_1, code_1)

# code_2 = encode(key_2, message)
# decoded_2 = decode(key_2, code_2)

# assert(code_1 == ";NB)3;E!6:82Uho;")
# assert(code_2 == "BC(;E;3;88#'oh;N")
# assert(message == decoded_1)
# assert(message == decoded_2)

# NOTE: YOU CAN DO MORE TESTS BY CHECKING DIFFERENT MESSAGES
