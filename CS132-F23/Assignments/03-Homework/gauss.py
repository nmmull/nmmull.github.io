import numpy as np

def leftmost_nonzero_index(a, row_index):
    """finds the leftmost nonzero entry after a given row

    parameters:

    a: 2D numpy array
    row_index: index for a row of A

    returns:

    (i, j) such that A[i, j] is the leftmost nonzero entry in A at or
    below the row ROW_INDEX, or None if no such value exists

    """
    nonzeros = np.transpose(np.nonzero(a[row_index:]))
    if len(nonzeros) != 0:
        l_r, l_c = min(nonzeros, key=lambda x: x[1])
        return l_r + row_index, l_c
    return None

def is_inconsistent_row(row):
    """checks if a row represents an inconsistent equation

    parameters:

    row: 1D numpy array

    returns:

    True if ROW is of the form [0 0 0 ... a] where a != 0, and False
    otherwise.

    """
    nonzeros = np.nonzero(row)[0]
    if len(nonzeros) != 0:
        return nonzeros[0] == len(row) - 1
    return False

def leading_entry_index(row):
    """finds the index of the leading entry of a row

    parameters:

    row: 1D numpy array

    returns:

    an index i such that ROW[i] is the leading entry (the first
    nonzero value) of ROW, or None if no such index exists

    """
    nonzeros = np.nonzero(row)[0]
    if len(nonzeros) != 0:
        return nonzeros[0]
    return None

def num_of_rows(a):
    """the number of rows if a matrix

    parameters:

    a: 2D numpy array

    returns:

    the number of rows of A

    """
    return a.shape[0]

def swap_rows(a, row_index_1, row_index_2):
    """swaps the rows of a matrix

    paramters:

    a: 2D numpy array
    row_index_1: index for a row of A
    row_index_2: index for a row of A

    returns:

    None

    A is mutated so that row ROW_INDEX_1 and row ROW_INDEX_2 are
    swapped

    """
    a[[row_index_1, row_index_2]] = a[[row_index_2, row_index_1]]

def zero_in_pivot_column(a, target_row_index, pivot_row_index, pivot_col_index):
    """subtracts a row with a pivot position from another row to
    zero-out a position at the pivot column index

    paramters:

    a: 2D numpy array
    target_row_index: index of a row of A
    pivot_row_index: row index of a pivot position of A
    pivot_col_index: column index of a pivot position of A

    returns:

    True if A[TARGET_ROW_INDEX] becomes inconsistent after mutation,
    and false otherwise

    A is mutated by

        A[TARGET_ROW_INDEX] -= c * A[PIVOT_ROW_INDEX]

    where c is chosen so that A[TARGET_ROW_INDEX, PIVOT_COL_INDEX] == 0.0

    sources:

    based on an implementation from the Jupyter Guide to Linear Algebra
    https://bvanderlei.github.io/jupyter-guide-to-linear-algebra/intro.html

    """
    tamp_row = np.vectorize(lambda x: 0.0 if np.isclose(x, 0.0) else x)
    pivot_val = a[pivot_row_index, pivot_col_index]
    elim_val = a[target_row_index, pivot_col_index]
    a[target_row_index] -= a[pivot_row_index] * elim_val / pivot_val
    a[target_row_index] = tamp_row(a[target_row_index])
    a[target_row_index, pivot_col_index] = 0.0
    return is_inconsistent_row(a[target_row_index])

def scale_to_one_in_pivot_column(a, pivot_row_index, pivot_col_index):
    """scales a pivot position to 1

    parameters:

    a: 2D numpy array
    pivot_row_index: row index of a pivot position
    pivot_col_index: column index of a pivot position

    returns:
    None

    A is mutated by

        A[PIVOT_ROW_INDEX] /= c

    where c is the entry at the pivot position of A

    """
    pivot_value = a[pivot_row_index, pivot_col_index]
    a[pivot_row_index] /= pivot_value

def elimination_phase(a):
    """converts a matrix into echelon form

    paramters:

    a: 2D numpy array

    returns:

    True if A represents an consistent system, and False otherwise

    A is mutated so that if A is consistent, it is converted into
    echelon form

    """
    for row_index in range(num_of_rows(a)):
        lm_index = leftmost_nonzero_index(a, row_index)
        if lm_index is None:
            break
        swap_rows(a, row_index, lm_index[0])
        for lower_row_index in range(row_index + 1, num_of_rows(a)):
            zero_in_pivot_column(a, lower_row_index, row_index, lm_index[1])
    return not any(map(is_inconsistent_row, list(a)))


def back_substitution_phase(a):
    """converts a matrix in echelon form into one in reduced echelon
    form

    parameters:
    a: 2D numpy array

    returns:

    None

    A is mutated so that if A is in echelon form, it is converted into
    reduced echelon form

    """
    for row_index in range(num_of_rows(a)):
        le_col_index = leading_entry_index(a[row_index])
        if le_col_index is not None:
            scale_to_one_in_pivot_column(a, row_index, le_col_index)
            for higher_row_index in range(row_index):
                zero_in_pivot_column(a, higher_row_index, row_index, le_col_index)

def gaussian_elimination(a):
    """converts a matrix into reduced echelon form

    parameters:

    a: 2D numpy array

    returns:

    None

    A is mutated so that is converted to reduced echelon form

    Note: back substitution should only be performed if A is
    consistent

    """
    if elimination_phase(a):
        back_substitution_phase(a)
