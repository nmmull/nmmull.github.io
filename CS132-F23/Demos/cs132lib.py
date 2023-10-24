import numpy as np

# Helpers

def num_of_rows(a):
    return a.shape[0]

def row_indices(a):
    return range(num_of_rows(a))

def rows(a):
    return a

def num_of_cols(a):
    return a.shape[1]

def col_indices(a):
    return range(num_of_cols(a))

def cols(a):
    return a.T

def swap_rows(a, i, j):
    a[[i, j]] = a[[j, i]]

def swap_cols(a, i, j):
    a = a.T
    swap_rows(a, i, j)
    a = a.T

def col_vec(v):
    return np.array([v]).T

def last_col(aug):
    return aug[:,-1]

def coeff_mat(aug):
    return aug[:,:-1]

def coin_flip(rng, p=0.5):
    return rng.random() > p

# Gaussian Elimination

def leftmost_nonzero_index(a, row_index):
    nonzeros = np.transpose(np.nonzero(a[row_index:]))
    if len(nonzeros) != 0:
        l_r, l_c = min(nonzeros, key=lambda x: x[1])
        return l_r + row_index, l_c

def subtract_row_to_zero_position(a, target_row_index, target_col_index, source_row_index):
    tamp_row = np.vectorize(lambda x: 0.0 if np.isclose(x, 0.0) else x)
    div_val = a[source_row_index, target_col_index]
    elim_val = a[target_row_index, target_col_index]
    a[target_row_index] -= a[source_row_index] * elim_val / div_val
    a[target_row_index] = tamp_row(a[target_row_index])
    a[target_row_index, target_col_index] = 0.0

def echelon_form(a):
    a = np.copy(a)
    for row_index in row_indices(a):
        lm_index = leftmost_nonzero_index(a, row_index)
        if lm_index is not None:
            lm_row_index, lm_col_index = lm_index
            swap_rows(a, row_index, lm_row_index)
            lm_row_index = row_index
            for lower_row_index in range(row_index + 1, num_of_rows(a)):
                subtract_row_to_zero_position(a, lower_row_index, lm_col_index, lm_row_index)
    return a

def reduced_echelon_form(a):
    a = echelon_form(a)
    for row_index in row_indices(a):
        leading_col_index = next(iter(np.nonzero(a[row_index])[0]), None)
        if leading_col_index is not None:
            a[row_index] /= a[row_index, leading_col_index]
            for higher_row_index in range(row_index):
                subtract_row_to_zero_position(a, higher_row_index, leading_col_index, row_index)
    return a

# Latex printing matrices

def lin_eq_latex(row):
    out = ""
    for i in range(len(row) - 1):
        coeff = int(row[i])
        if out == "":
            coeff_str = str(coeff)
            coeff_str = f'({coeff_str})' if coeff < 0 else coeff_str
            if coeff == -1: coeff_str = '-'
            if coeff == 1: coeff_str = ''
            if coeff != 0:
                out += f'{coeff_str}x_{i + 1}'
        else:
            op = '+'
            if coeff < 0: op = '-'
            coeff_str = str(abs(coeff)) if abs(coeff) != 1 else ""
            if coeff != 0:
                out += f' {op} {coeff_str}x_{i + 1}'
    if out == "":
        return f'0 &= {int(row[-1])} \\\\'
    out = out + f' &= {int(row[-1])} \\\\'
    return out

def lin_sys_latex(a):
    out = "\\begin{align*}\n"
    for row in a:
        out += f'  {lin_eq_latex(row)}\n'
    return out + "\\end{align*}"

def bmatrix_row_latex(row):
    out = ""
    for elem in row:
        out += f'{int(elem)} & '
    return out[:-2] + "\\\\"

def bmatrix_latex(a):
    out = "\\begin{bmatrix}\n"
    for row in a:
        out += f'  {bmatrix_row_latex(row)}\n'
    return out[:-4] + "\n\\end{bmatrix}"

def vec_latex(v):
    return bmatrix_latex(col_vec(v))

def matrix_eq_latex(aug):
    out = ""
    out += f'{bmatrix_latex(coeff_mat(aug))}\n'
    out += "\\mathbf x =\n"
    out += f'{vec_latex(last_col(aug))}'
    return out

def set_of_vec_latex(a):
    out = "\\left\\{\n"
    for col in cols(a):
        out += f'{vec_latex(col)},\n'
    return out[:-2] + "\n\\right\\}"

def list_of_vec_latex(a, letter):
    out = ""
    for i in col_indices(a):
        out += f'\\mathbf {letter}_{i + 1} =\n{vec_latex(a[:,i])}\n'
    return out

# Random systems

def ref_gen(shape, seed=None, coeff_range=(-5, 5)):
    rng = np.random.default_rng(seed)
    a = np.zeros(shape)
    piv_row = 0
    for i in col_indices(a):
        if coin_flip(rng, 1. / max(shape[0], shape[1])) and piv_row < num_of_rows(a):
            a[piv_row, i] = 1
            piv_row += 1
        else:
            for j in range(piv_row):
                a[j, i] = rng.integers(coeff_range[0], coeff_range[1])
    return a

def problem_gen(aug, seed=None, scale_range=(-2, 2)):
    rng = np.random.default_rng(seed)
    aug = np.copy(aug)
    for i in row_indices(aug):
        for j in row_indices(aug):
            if j != i:
                aug[i] += rng.integers(scale_range[0], scale_range[1]) * aug[j]
    return aug

def aug_gen(shape, seed=None, rhs_range=(-10, 10), scale_range=(-2, 2)):
    rng = np.random.default_rng(seed)
    ref = ref_gen(shape, rng)
    b = rng.integers(rhs_range[0], rhs_range[1], shape[0])
    print(ref)
    print(b)
    aug = np.hstack([ref, col_vec(b)])
    return (aug, problem_gen(aug, rng, scale_range))
