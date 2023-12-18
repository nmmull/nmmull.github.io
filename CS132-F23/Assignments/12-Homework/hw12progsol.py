import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

def dist(x, y):
    """Computes the distance between two vectors

    Parameters:

    x: 1D NumPy array
    y: 1D NumPy array

    Returns: dist(x, y) = || x - y ||

    """
    # >>>>>>>>>>
    return np.linalg.norm(x - y)
    # >>>>>>>>>>
    # TODO: Fill in this function and change the return value
    return 0.0

def linear_design_matrix(ind_vars):
    """Builds the design matrix for fitting a linear function to a
    dataset

    Parameters:

    ind_vars: 2D NumPy array, where each row represents the
    independent variables of a single data point

    Return:

    The design matrix for fitting a plane to the data in ind_vars, i.e., the matrix

        [   1s   ind_vars   ]

    """
    # >>>>>>>>>>
    return np.column_stack((np.ones(ind_vars.shape[0]), ind_vars))
    # >>>>>>>>>>
    # TODO: Fill in this function and change the return value
    return ind_vars

def quadratic_design_matrix(ind_vars):
    """Builds the design matrix for fitting a quadratic function to a
    dataset

    Parameters:

    ind_vars: 2D NumPy array, where each row represents the
    independent variables of a single data point

    Return:

    The design matrix for fitting a quadratic function to the data in
    ind_vars (see the problem description for more details).

    """
    # >>>>>>>>>>
    X_quad = linear_design_matrix(ind_vars)
    for i in range(ind_vars.shape[1]):
        for j in range(i, ind_vars.shape[1]):
            X_quad = np.column_stack((X_quad, ind_vars[:, i] * ind_vars[:, j]))
    return X_quad
    # >>>>>>>>>>
    # TODO: Fill in this function and change the return value
    return ind_vars

def cubic_design_matrix(ind_vars):
    """Builds the design matrix for fitting a cubic function to a
    dataset

    Parameters:

    ind_vars: 2D NumPy array, where each row represents the
    independent variables of a single data point

    Return:

    The design matrix for fitting a cubic function to the data in
    ind_vars (see the problem description for more details).

    """
    # >>>>>>>>>>
    X_cubic = quadratic_design_matrix(ind_vars)
    for i in range(ind_vars.shape[1]):
        for j in range(i, ind_vars.shape[1]):
            for k in range(j, ind_vars.shape[1]):
                X_cubic = np.column_stack((X_cubic, ind_vars[:, i] * ind_vars[:, j] * ind_vars[:, k]))
    return X_cubic
    # >>>>>>>>>>
    # TODO: Fill in this function and change the return value
    return ind_vars

def fit(design_matrix, observations):
    """Finds a model determined by the a design matrix and
    observations

    Parameters:

    design_matrix: 2D NumPy array, representing a design matrix
    observations: 1D NumPy array, representing observations

    Returns:

    A tuple with (1) the least squares solution to the equation

        design_matrix @ beta == observations

    (2) the predicted values and (3) the distance between the
    predicted values and the observations

    """
    parameters = np.linalg.lstsq(design_matrix, observations, rcond=None)[0]
    prediction = design_matrix @ parameters
    return (parameters, prediction, dist(prediction, observations))

housing = fetch_california_housing()
ind_vars = housing.data
dep_vars = housing.target

_, y_hat_line, error_line = fit(linear_design_matrix(ind_vars), dep_vars)
_, y_hat_quad, error_quad = fit(quadratic_design_matrix(ind_vars), dep_vars)
_, y_hat_cube, error_cube = fit(cubic_design_matrix(ind_vars), dep_vars)

print("======")
print("REPORT")
print("======")
print()
print("Dataset Info")
print("------------")
print("    - Number of data points: 20640")
print()
print("    - Independent variables: (8 total)")
print()
for line in housing.DESCR.splitlines()[12:20]:
    print(line)
print()
print("    - Dependent variable: median house value (multiples of $100,000)")
print()
print("    - Note: from 1990 census, each row represents a single district")
print()
print("Prediction Error")
print("----------------")
print(f'   linear func. model:   {error_line}')
print(f'quadratic func. model:   {error_quad}')
print(f'    cubic func. model:   {error_cube}')

# Plots predictions against the actual values, as in the notes
# The closer to the red line, the better the prediction
# Uncomment below if you want to see the plot
# Switch out the predicted values and compare the plots
# NOTE: YOU DON'T HAVE TO SUBMIT ANYTHING FOR THIS
#       IT'S JUST FOR FUN

# plt.scatter(dep_vars, y_hat_cube)
# plt.plot([0, 5], [0, 5], color='red')
# plt.show()
