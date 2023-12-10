import numpy as np

# 1: Basic Analytic Geometry

v = np.array([1., -1, 5,  7, 4])
u = np.array([3.,  1, 3, -1, 0])

# A
assert(np.isclose(np.sqrt(v @ v), np.sqrt(92)))

# B

norm_u = np.sqrt(u @ u)
unit_u = u / norm_u

answer = (1 / np.sqrt(20)) * np.array([3, 1, 3, -1, 0])
assert(np.allclose(unit_u, answer))

# C
assert(np.isclose(np.sqrt((u - v) @ (u - v)), np.sqrt(92)))

# D

cos_theta = (u @ v) / np.sqrt(u @ u) / np.sqrt(v @ v)
theta_rad = np.arccos(cos_theta)
theta_deg = np.round(theta_rad * 180 / np.pi, 1)

assert(theta_deg == 76.5)

# E

angle = 180 - 2 * theta_deg

cos = (v @ (v - u)) / np.sqrt(v @ v) / np.sqrt((u - v) @ (u - v))
rad = np.arccos(cos)
answer = np.round(rad * 180 / np.pi, 1)

assert(angle == answer)

# 2: The Gram-Schmidt Process

v1 = np.array([1,  0, 1,  1])
v2 = np.array([0,  1, 1,  2])
v3 = np.array([1,  0, 2, -2])
u  = np.array([2, -2, 1, -5])

assert(np.allclose(u, v1 - 2 * v2 + v3))

# A

v2_hat = (v2 @ v1) / (v1 @ v1) * v1
assert(np.allclose(v2_hat, v1))

v2_0 = v2 - v2_hat
assert(np.allclose(v2_0, np.array([-1, 1, 0, 1])))

# B

v3_hat = (v3 @ v1) / (v1 @ v1) * v1
assert(np.allclose(v3_hat, 1 / 3 * v1))

v3_0 = v3 - v3_hat
assert(np.allclose(v3_0, np.array([2/3, 0, 5/3, -7/3])))

# C

v3_0_hat = (v3_0 @ v2_0) / (v2_0 @ v2_0) * v2_0
assert(np.allclose(v3_0_hat, np.array([1, -1, 0, -1])))

v3_00 = v3_0 - v3_0_hat
assert(np.allclose(v3_00, np.array([-1/3, 1, 5/3, -4/3])))

# D

assert(np.isclose(v1 @ v2_0, 0))
assert(np.isclose(v2_0 @ v3_00, 0))
assert(np.isclose(v3_00 @ v1, 0))

# E

u_b = np.array([
    (u @ v1) / (v1 @ v1),
    (u @ v2_0) / (v2_0 @ v2_0),
    (u @ v3_00) / (v3_00 @ v3_00)])

assert(np.allclose(u_b, np.array([-2/3, -3, 1])))

# 3: Orthogonal Projection Matrices

v = np.array([2, 3, 1])
a = np.array([
    [1., 2, -5],
    [1, 1, 3],
    [8, 14, -6],
    [1, 2, 1]])

b = np.array([
    [1., 0, 3, 0],
    [-4, 2, -5, 1],
    [-2, 2, 1, 1],
    [9, -6, 9, -2],
    [0, 1, 5, 1]]).T

# A

c1 = (v @ np.eye(3)[0]) / (v @ v) * v
c2 = (v @ np.eye(3)[1]) / (v @ v) * v
c3 = (v @ np.eye(3)[2]) / (v @ v) * v

m = np.array([c1, c2, c3]).T

assert(np.allclose(m, np.outer(v, v) / 14))

# B

assert(np.allclose(m, (np.array([v]).T @ np.array([v])) / (v @ v)))

# C

assert(np.linalg.matrix_rank(a) == 3)

proj_col_a = a @ np.linalg.inv(a.T @ a) @ a.T

# D =

assert(np.linalg.matrix_rank(b) == 3)
assert(np.linalg.matrix_rank(b[:,:3]) == 2)
assert(np.linalg.matrix_rank(b[:,:4]) == 3)

b0 = b[:,[0, 1, 3]]

proj_col_b = b0 @ np.linalg.inv(b0.T @ b0) @ b0.T

# E

assert(np.allclose(proj_col_a, proj_col_b))

# 4: Least Squares

a = np.array([
    [1, 2],
    [0, -1],
    [1, -1]])
b = np.array([4, 2, 0])

U = np.array([
    [1., 0, 1],
    [1., 0, 1],
    [1., 0, 1],
    [1, 1, 0],
    [1, 1, 0],
    [1, 1, 0]])
c = np.array([6, 5, 4, 7, 2, 3])

# A

assert(np.allclose(a.T @ a, np.array([
    [2, 1],
    [1, 6]])))

assert(np.allclose(a.T @ b, np.array([4, 6])))

# B

assert(np.allclose(np.linalg.inv(a.T @ a), np.array([
    [6, -1],
    [-1, 2]]) / 11))

sol = np.linalg.inv(a.T @ a) @ a.T @ b
assert(np.allclose(sol, np.array([18 / 11, 8 / 11])))

# D

assert(np.allclose(U.T @ U, np.array([
    [6., 3, 3],
    [3, 3, 0],
    [3, 0, 3]])))

assert(np.allclose(U.T @ c , np.array([27, 12, 15])))

# E

aug = np.array([
    [6., 3, 3, 27],
    [3, 3, 0, 12],
    [3, 0, 3, 15]])
aug /= 3
aug[[0, 1]] = aug[[1, 0]]
aug[1] -= 2 * aug[0]
aug[2] -= aug[0]
aug[2] -= aug[1]
aug[0] += aug[1]
aug[1] *= -1

assert(np.allclose(aug, np.array([
    [1., 0, 1, 5],
    [0, 1, -1, -1],
    [0, 0, 0, 0]])))

# x1 = 5 - x3
# x2 = -1 + x3
# x3 is free

sol1 = np.array([5., -1, 0])
sol2 = np.array([4., 0, 1])

assert(np.allclose(U.T @ U @ sol1, U.T @ c))
assert(np.allclose(U.T @ U @ sol2, U.T @ c))
assert(np.linalg.matrix_rank(np.array([sol1, sol2]).T) == 2)
