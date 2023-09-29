import numpy as np
from gauss import elimination_phase

# Note: None of the following code performs any error handling, e.g.,
# the behavior of matrix-vector multiplication is only well-defined on
# well-defined inputs

def mat_eq(a, b):
    """checks if two matrices are equal

    parameters:

    a: 2D numpy array
    b: 2D numpy array

    returns:

    True if a and b are the same (up to np.isclose) and 0 otherwise.

    """
    return np.isclose(a, b).all()

def vec_eq(u, v):
    """checks if two matrices are equal

    parameters:

    u: 1D numpy array
    v: 1D numpy array

    returns:

    True if u and v are the same (up to np.isclose) and 0 otherwise.

    """
    return mat_eq(u, v)

def mat_vec_mul(a, v):
    """multiplies a matrix with a vector

    parameters:

    a: 2D numpy array
    v: 1D numpy array

    returns:

    a times v

    """
    return a @ v

def mat_of_vecs(vs):
    """creates a matrix out of a list of column vectors

    parameters:

    vs: list of 1D numpy arrays

    returns:

    the matrix whose columns are in VS, i.e.,

    mat_of_vecs([v1, v2, v3]) = [ v1 v2 ... vn ]

    """
    return np.array(vs).T

def vecs_of_mat(a):
    """creates a list of column vectors from a matrix

    parameters:

    a: 2D numpy array

    returns:

    list of vectors which are the columns of A, i.e.,

    vecs_of_mat([v1 v2 v3]) = [v1, v2, v3]

    """
    return list(a.T)

def add_col(a, v):
    """adds a column to a matrix

    parameters:

    a: 2D numpy array
    v: 1D numpy array

    returns:

    the matrix [a v]

    """
    return np.hstack((a, np.array([v]).T))

def is_consistent_aug(a):
    """checks if an augmented matrix is consistent

    parameters:

    a: 2D numpy array representing an augmented matrix

    returns:

    True if A represents the augmented matrix of a consistent system
    of linear equations, and False otherwise.

    """
    return elimination_phase(a)

def is_consistent_mat_eq(a, b):
    """checks if a matrix equation is consistent

    parameters:

    a: 2D numpy array
    b: 1D numpy array

    returns:

    True if Ax = B is consistent, and False otherwise.

    """
    # >>>>>>>>>>
    return is_consistent_aug(add_col(a, b))
    # >>>>>>>>>>
    # TODO: fill in this function and change the return value
    return None


def is_consistent_vec_eq(vs, b):
    """checks if a vector equation is consistent

    parameters:

    vs: list of 1D numpy arrays
    b: 1D numpy array

    returns:

    Given VS = [v1, v2,...,vn]

    True if x1 * v1 + x2 * v2 + ... + xn * vn is consistent, and False
    otherwise.

    """
    # >>>>>>>>>>
    return is_consistent_mat_eq(mat_of_vecs(vs), b)
    # >>>>>>>>>>
    # TODO: fill in this function and change the return value
    return None


def in_span(u, vs):
    """checks if a vector is in the span of a list of vectors

    parameters:

    u: 1D numpy array
    vs: list of 1D numpy arrays

    all numpy arrays must be the same size

    returns:

    True if U lies in the span of VS and False otherwise.

    """
    # >>>>>>>>>>
    return is_consistent_vec_eq(vs, u)
    # >>>>>>>>>>
    # TODO: fill in this function and change the return value
    return None

def num_of_rows(a):
    """returns the number of rows of a 2D numpy array A"""
    return a.shape[0]

def num_of_columns(a):
    """returns the number of columns of a 2D numpy array A"""
    return a.shape[1]

def num_of_pivots(a):
    """returns the number of pivot positions in a matrix

    parameters:

    a: 2D numpy array

    returns:

    the number of pivot positions of A

    """
    # >>>>>>>>>>
    elimination_phase(a)
    return sum(map(lambda x: len(np.nonzero(x)[0]) != 0, list(a)))
    # >>>>>>>>>>
    # TODO: fill in this function and change the return value
    return None

def full_span_cols(a):
    """checks if the columns of a matrix have full span

    parameters:

    a: 2D numpy array

    returns:

    True if the columns of A span all of Rn, given that A has n rows,
    and False otherwise

    """
    # >>>>>>>>>>
    return num_of_pivots(a) == a.shape[0]
    # >>>>>>>>>>
    # TODO: fill in this function and change the return value
    return None

def full_span(vs):
    """checks if a list of vectors have full span

    parameters:

    vs: list of 1D numpy arrays

    returns:

    True if the vectors in VS span all of Rn, given that the vectors
    in VS have n entries, and False otherwise

    """
    # >>>>>>>>>>
    return full_span_cols(mat_of_vecs(vs))
    # >>>>>>>>>>
    # TODO: fill in this function and change the return value
    return None

def lin_ind_cols(a):
    """checks if the columns of a matrix are linearly independent

    parameters:

    a: 2D numpy array

    returns:

    True if the columns of A are linearly independent, and False
    otherwise

    """
    # >>>>>>>>>>
    return num_of_pivots(a) == a.shape[1]
    # >>>>>>>>>>
    #TODO: fill in this function and change the return value
    return None

def lin_ind(vs):
    """checks if a list of vectors is linearly independent

    parameters:

    vs: list of 1D numpy arrays

    returns:

    True if the vectors in VS are linearly independent, and False
    otherwise

    """
    # >>>>>>>>>>
    return lin_ind_cols(mat_of_vecs(vs))
    # >>>>>>>>>>
    # TODO: fill in this function and change the return value
    return None
