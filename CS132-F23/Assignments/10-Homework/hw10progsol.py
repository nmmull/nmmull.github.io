import numpy as np

def power_step(a, v, zero_cols, alpha=0.15):
    """Performs one step of the power method

    Parameters:

    a: 2D sparce SciPy matrix
    v: 1D NumPy array
    zero_cols: 1D NumPy array
    alpha: float for the damping factor

    Returns:

    The result of performing one step of the power method, including
    reflecting boundaries and damping

    Roughly speaking, it should return the vector

    (1 - alpha)(av + (1/n)w) + (alpha/n)u

    where w and u are vectors which represent boundary reflection and
    damping, respectively

    Notes:

    zero_col has the property that zero_col[i] == 1 if column i of 'a'
    is all zeros, and zero_col[i] == 0 otherwise.

    """
    # >>>>>>>>>>
    return (1 - alpha) * (a.dot(v) + (zero_cols @ v) / a.shape[1]) + alpha * np.sum(v) / a.shape[1]
    # >>>>>>>>>>
    # TODO: Fill in this function and change its return value
    return None

def print_error_log(num_iter, s):
    print(f'    | error after {num_iter} iterations: {s}')

def l1_error(u, v):
    """Computes the L1 error of two vectors

    Parameters:

    u: 1D NumPy array
    v: 1D NumPy array

    Returns:

    The sum of the absolute values of the differences of the entries
    of u and v

    """
    # >>>>>>>>>>
    return np.sum(np.abs(u - v))
    # >>>>>>>>>>
    # TODO: Fill in this function and change its return value
    return None

def power_iter(a, start, zero_cols, tol=0.001, alpha=0.15):
    """Computes a steady state via the power method

    Parameters:

    a: 2D sparse SciPy matrix
    start: 1D NumPy matrix, starting point for the power method
    zero_cols: 1D NumPy array (see docstring for power_step)
    tol: float for error tolerance
    alpha: float for the damping factor

    Returns:

    The result of repeated applications of power_step until the
    l1_error between consecutive vectors is below the given error
    tolerance

    Notes:

    It should call print_error_log every 10 iterations, and one last
    time for the last iteration

    """
    # >>>>>>>>>>
    last = start
    curr = power_step(a, last, zero_cols)
    num_iter = 1
    while True:
        err = l1_error(curr, last)
        if err < tol:
            print_error_log(num_iter, err)
            break
        if num_iter % 10 == 0:
            print_error_log(num_iter, err)
        curr, last = power_step(a, curr, zero_cols), curr
        num_iter += 1
    return curr
    # >>>>>>>>>>
    # TODO: Fill in this function and change its return value
    return None

top_five_stanford = [] # TODO: Fill this in
top_five_berkstan = [] # TODO: Fill this in
top_five_google = [] # TODO: Fill this in
# >>>>>>>>>>
top_five_stanford = [281, 67, 1352, 4898, 3367]
top_five_berkstan = [288238, 9, 225465, 54130, 1283]
top_five_google = [115, 2138, 2560, 3178, 1950]
# >>>>>>>>>>
