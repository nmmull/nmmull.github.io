import numpy as np

def inner_product(u: np.array, v: np.array) -> float:
    """computes the inner product of two vectors

    Paramters:

    u: 1D numpy array
    v: 1D numpy array

    Preconditions:

    u.ndim == 1                # u is a 1D array
    v.ndim == 1                # v is a 1D array
    str(u.dtype) == 'float64'  # u is a vector of floats
    str(v.dtype) == 'float64'  # v is a vector of floats
    u.shape[0] == v.shape[0]   # the vectors are the same size

    Returns:

    u1 * v1 + u2 * v2 + ... + un * vn

    Example:

    >>> inner_product(np.array([1., 2, 0]), np.array([3., 1, 0]))
    5.0

    """
    # >>>>>>>>>>
    return sum(map(lambda p: p[0] * p[1], zip(list(u), list(v))))
    # >>>>>>>>>>
    # TODO: fill in this function and change the return value
    return 0.0

def column(a: np.array, i: int) -> np.array:
    """returns the column of a matrix at a given index

    Parameters:

    a: 2D numpy array
    i: index for a column of a

    Preconditions:

    a.ndim == 2                # a is 2 dimensional
    0 <= i and i < a.shape[1]  # i is a valid index

    Returns:

    the i-th column of a

    Example:

    >>> column(np.array([[0., 1], [1, 0]]), 1)
    array([1., 0.])

    """
    # Note this for future reference
    # Make sure you understand how it works
    return a[:, i]

def mat_vec_mult_ip(a: np.array, v: np.array) -> np.array:
    """computes matrix-vector multiplication via the row-column rule

    Parameters:

    a: 2D numpy array
    v: 1D numpy array

    Preconditions:

    str(a.dtype) == 'float64'
    str(v.dtype) == 'float64'
    a.ndim == 2
    v.ndim == 1
    a.shape[1] == v.shape[0] # num of cols of a == num of rows of v

    Returns:

    a * v (computed via the row-column rule)

    Example:

    >>> mat_vec_mult_ip(np.array([[2., 0], [0, 3]]), np.array([1., 1]))
    array([2., 3.])

    """
    # >>>>>>>>>>
    out = []
    for row in a:
        out.append(inner_product(row, v))
    return np.array(out)
    # >>>>>>>>>>
    # TODO: fill in this function and change the return value
    return np.array([])

def mat_vec_mult_vs(a: np.array, v: np.array) -> np.array:
    """computes matrix-vector multiplication via the linear combination of columns

    Parameters:

    a: 2D numpy array
    v: 1D numpy array

    Preconditions:

    str(dtype(a)) == 'float64'
    str(dtype(v)) == 'float64'
    a.ndim == 2
    v.ndim == 1
    a.shape[1] == v.shape[0]

    Returns:

    a * v (computed as v1 * a1 + v2 * a2 + ... + vn * an)

    Example:
    >>> mat_vec_mult_vs(np.array([[2., 0], [0, 3]]), np.array([1., 1]))
    array([2., 3.])

    """
    # >>>>>>>>>>
    out = np.zeros(a.shape[0])
    for i in range(a.shape[1]):
        out += v[i] * column(a, i)
    return out
    # >>>>>>>>>>
    # TODO: fill in this function and change the return value
    return np.array([])
