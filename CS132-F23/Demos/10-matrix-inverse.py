import numpy as np

# invertible matrix
a = np.array(
    [[1., 2, 5],
     [0, 1, 3],
     [1, 0, 0]])

# inverse of a
ainv = np.linalg.inv(a)

# a with the identity on the right
aid = np.hstack([a, np.eye(3)])

# row reductions
# TODO
aid[2] -= aid[0]
aid[2] += 2 * aid[1]
aid[1] -= 3 * aid[2]
aid[0] -= 5 * aid[2]
aid[0] -= 2 * aid[1]

print()
print(aid)

print()
print("inverse of a:")
print(ainv)

# inverse of a (again)
b = aid[:,3:]
print()
print("a times calculated inverse:")
print(a @ b)
