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
    # TODO: Fill in this function and change its return value
    return None

top_five_stanford = [] # TODO: Fill this in
top_five_berkstan = [] # TODO: Fill this in
top_five_google = [] # TODO: Fill this in
